from pl_token import *

# class Expression:
#     def __init__(self, left, operator, right):
#         self.left = left
#         self.operator = operator
#         self.right = right
#
#     def evaluate(self):
#         if self.operator == '+':
#             return int(self.left ) + int(self.right)
#         elif self.operator == '*':
#             return int(self.left) * int(self.right)
#         else:
#             return int(self.left)

class PlParser:
    """
    Parser - finds the  structure in the stream of tokens
    """
    # register_dict = {"R0": None, "R1": None, "R2": None, "R3": None, "R4": None,
    #                  "R5": None, "R6": None, "R7": None, "R8": None, "R9": None}

    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()
        self.current_command = self.__update_command()
        # self.register_x = None
        # self.register_y = None
        # self.if_operator = None
        # self.goto_label = None
        # self.expression = None
        # self.register_dict = {"R0": None, "R1": None, "R2": None, "R3": None, "R4": None,
        #                       "R5": None, "R6": None, "R7": None, "R8": None, "R9": None}

    def __str__(self):
        return f"Lexer object: {self.lexer}, current_token object: {self.current_token}"

    def __repr__(self):
        return self.__str__()

    # @staticmethod
    # def print_registers():
    #     print()
    #     print("All registers:")
    #     for i in range(0, 10):
    #         print(f"R{i}: {PlParser.register_dict[str('R' + str(i))]}")

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    # def read_reg(self, reg):
    #     if PlParser.register_dict[reg] != None:
    #         return PlParser.register_dict[reg]
    #     else:
    #         raise Exception(f'Register {reg} is not defined!')

    def get_current_token(self):
        return self.current_token

    def __update_command(self):
        """
             Checks if current token is the command or label, stores in parser what is current command name
             or "LABEL" token if it's label type
             :return: current command name or "LABEL"
             :rtype: string
        """
        if self.current_token.value in RESERVED_COMMANDS.keys():
            return self.current_token.value
        elif self.current_token.type == LABEL:
            return "LABEL"

    def get_command(self):
        """
        Returns current command as stored in parser object
        :return: current command name or "LABEL"
        :rtype: string
        """
        return self.current_command

    # def parse_expression(self):
    #     left, operator, right = None, None, None
    #
    #     if self.current_token.type == REGISTER:
    #         left = self.read_reg(self.current_token.value)
    #         self.eat(REGISTER)
    #     else:
    #         left = self.current_token.value
    #         self.eat(INTEGER_CONST)
    #
    #     if self.current_token.type == PLUS:
    #         operator = self.current_token.value
    #         self.eat(PLUS)
    #     elif self.current_token.type == MINUS:
    #         operator = self.current_token.value
    #         self.eat(MINUS)
    #     else:
    #         self.eat(EOL)
    #
    #     if operator != None:
    #         if self.current_token.type == REGISTER:
    #             right = self.read_reg(self.current_token.value)
    #             self.eat(REGISTER)
    #         else:
    #             right = self.current_token.value
    #             self.eat(INTEGER_CONST)
    #
    #     self.expression = Expression(left, operator, right)

    # def let_command_parser(self):
    #     self.eat(COMMAND)
    #     self.register_x = self.current_token.value
    #     self.eat(REGISTER)
    #
    #     self.eat(ASSIGN)
    #
    #     self.parse_expression()

    # def let_command_evaluate(self):
    #     PlParser.register_dict[self.register_x] = self.expression.evaluate()

    # def if_command_parser(self):
    #     self.eat(COMMAND)
    #
    #     self.register_x = self.current_token.value
    #     self.eat(REGISTER)
    #
    #     self.if_operator = self.current_token.value
    #     self.eat(IF_OPERATOR)
    #
    #     self.register_y = self.current_token.value
    #     self.eat(REGISTER)
    #
    #     self.goto_label = self.current_token.value
    #     self.eat(GOTO_LABEL)

    # def if_command_evaluate(self):
    #     rx = PlParser.register_dict[self.register_x]
    #     ry = PlParser.register_dict[self.register_y]
    #     if rx != None and ry != None:
    #         match self.if_operator:
    #             case '=':
    #                 if rx == ry:
    #                     return True
    #             case '<':
    #                 if rx < ry:
    #                     return True
    #             case '>':
    #                 if rx > ry:
    #                     return True
    #             case default:
    #                 raise Exception('Invalid if_operator!')
    #         return False
    #     else:
    #         raise Exception('IF operation register operand is not initialized!')

    # def jump_command_parser(self):
    #     self.eat(COMMAND)
    #     self.goto_label = self.current_token.value
    #     self.eat(GOTO_LABEL)

    # def print_command_parser(self):
    #     self.eat(COMMAND)
    #     self.register_x = self.current_token.value
    #     self.eat(REGISTER)

    # def print_command_evaluate(self):
    #     rx = PlParser.register_dict[self.register_x]
    #     if rx != None:
    #         print(f"{self.register_x}: {rx}")
    #     else:
    #         raise Exception('Cannot print the value of register, register not initialized!')
    def parse(self):
        """
        Parser - does parsing of single command line of the program
        :return:
        :rtype:
        """
        #self.get_command()
        # self.eat(COMMAND)

        # match self.current_command:
        #      case "LET":
        #           pass
        #      case "IF":
        #          self.if_command_parser()
        #      case "JUMP":
        #          self.jump_command_parser()
        #      case "CALL":
        #          self.jump_command_parser()
        #      case "RETURN":
        #          pass
        #      case "PRINT":
        #          self.print_command_parser()
        #      case "LABEL":
        #          pass
        #      case default:
        #          pass

        # if self.current_token.type == EOF:
        #     self.error()

        # return self.current_command

    def evaluate(self):
        return None
        # match self.current_command:
        #     case "LET":
        #         pass
        #         return None
        #     case "IF":
        #         condition_result = self.if_command_evaluate()
        #         if condition_result:
        #             return self.goto_label
        #         else:
        #             return None
        #     case "JUMP":
        #         return self.goto_label
        #     case "CALL":
        #         return self.goto_label
        #     case "RETURN":
        #         return None
        #     case "PRINT":
        #         return self.print_command_evaluate()
        #     case "LABEL":
        #         return None
        #     case default:
        #         return None