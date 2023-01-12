
import sys
from src.spl_lexer import *
from src.spl_parser import *
from src.spl_let_command_parser import *
from src.spl_if_command_parser import *
from src.spl_registers import SPlRegisters
from src.spl_jump_command_parser import *
from src.spl_call_command_parser import *
from src.spl_return_command_parser import *
from src.spl_print_command_parser import *

# input_lines - the list of all input lines from the input program
input_lines = []
# label_dict - stores the dictionary of number of lines per label from input program file {label_name: line_num}
label_dict = {}
last_call_return_line = 0

class SPlInterpreter:
    def __init__(self, path_to_input_file):
        self.input_file_path = path_to_input_file


    def enumerate_input_lines(self):
        """
        Reads all lines of input program into the list of lines - input_lines global variable
        :return: None
        :rtype: None
        """
        with open(self.input_file_path, 'r') as f:
            global input_lines
            input_lines = f.readlines()


    def update_label_dict(self):
        """
        Enumerate all input lines. Go line after line and parse it's first token (=command).
        If first token is of type label then trims colon from it and stores it and the number
        of line in label_dict structure
        :return: none
        :rtype: none
        """
        global label_dict

        en_input_lines = enumerate(input_lines)
        for line in list(en_input_lines):
            lexer = Lexer(line[1])
            #parser = SPlParser(lexer)
            #command = parser.get_command()
            command = self.get_command_name(lexer)
            if command == "LABEL":
                token = lexer.get_current_token()
                trim_colon_label = token.value[:-1] # bring the Label without the colon
                label_dict[trim_colon_label] = line[0]

    def get_command_name(self, lexer):
        if lexer.get_current_token().value in RESERVED_COMMANDS.keys():
            return lexer.get_current_token().value
        elif lexer.get_current_token().type == LABEL:
            return "LABEL"

    def get_command_object(self,command_name, lexer):
        match command_name:
            case "LET":
                return LetCommandParser(lexer)
            case "IF":
                return IfCommandParser(lexer)
            case "JUMP":
                return JumpCommandParser(lexer)
            case "CALL":
                return CallCommandParser(lexer)
            case "RETURN":
                return ReturnCommandParser(lexer)
            case "PRINT":
                return PrintCommandParser(lexer)
            case "LABEL":
                return None
            case default:
                raise Exception(f'{command_name} command is not defined!')


    def interpret_file(self):
        self.enumerate_input_lines()
        self.update_label_dict()

        token = ("LABEL", "START")
        global label_dict
        global input_lines
        global last_call_return_line

        en_input_lines = enumerate(input_lines)
        while token != ("LABEL", "END"):
            goto_label = None
            for line in list(en_input_lines):
                lexer = Lexer(line[1])
                #parser = SPlParser(lexer)
                cmd_name = self.get_command_name(lexer)
                cmd = self.get_command_object(cmd_name, lexer)
                if cmd is not None:
                    cmd.parse()
                    goto_label = cmd.evaluate()

                match cmd_name:
                    case "LET":
                        token = ("COMMAND", "LET")
                    case "IF":
                        if goto_label == None:
                            token = ("COMMAND", "IF")
                        else:
                            line_num = label_dict[goto_label]
                            token = ("LABEL", goto_label)
                            en_input_lines = enumerate(input_lines[line_num:], line_num)
                            break

                    case "JUMP":
                        line_num = label_dict[goto_label]
                        token = ("LABEL", goto_label)
                        en_input_lines = enumerate(input_lines[line_num:], line_num)
                        break

                    case "CALL":
                        last_call_return_line = line[0] + 1

                        line_num = label_dict[goto_label]
                        token = ("LABEL", goto_label)
                        en_input_lines = enumerate(input_lines[line_num:], line_num)
                        break

                    case "RETURN":
                        en_input_lines = enumerate(input_lines[last_call_return_line:], last_call_return_line)
                        token = ("COMMAND", "RETURN")
                        break

                    case "PRINT":
                        token = ("COMMAND", "PRINT")

                    case "LABEL":
                        token = ("LABEL", lexer.get_current_token().value[:-1]) # trim the colon from the label

                    case default:
                        raise Exception(f'{cmd_name} command is not defined!')


if __name__ == '__main__':
    pl_interpreter = SPlInterpreter(sys.argv[1])
    pl_interpreter.interpret_file()
    SPlRegisters.print_registers()
