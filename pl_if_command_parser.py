from pl_parser import PlParser
from pl_token import *
from pl_registers import PlRegisters

class IfCommandParser(PlParser):
    def __init__(self, lexer):
        super().__init__(lexer)
        self.register_x = None
        self.register_y = None
        self.if_operator = None
        self.goto_label = None

    def parse(self):
        self.register_x = self.current_token.value
        self.eat(REGISTER)

        self.if_operator = self.current_token.value
        self.eat(IF_OPERATOR)

        self.register_y = self.current_token.value
        self.eat(REGISTER)

        self.goto_label = self.current_token.value
        self.eat(GOTO_LABEL)

    def evaluate(self):
        condition_result = False
        rx = PlRegisters.read_reg(self.register_x)
        ry = PlRegisters.read_reg(self.register_y)
        if rx != None and ry != None:
            match self.if_operator:
                case '=':
                    if rx == ry:
                        condition_result =  True
                case '<':
                    if rx < ry:
                        condition_result = True
                case '>':
                    if rx > ry:
                        condition_result = True
                case default:
                    raise Exception('Invalid if_operator!')

            if condition_result == True:
                return self.goto_label
            else:
                return None

        else:
            raise Exception('IF operation register operand is not initialized!')