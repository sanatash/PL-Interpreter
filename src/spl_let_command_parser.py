from src.spl_parser import SPlParser
from src.spl_token import *
from src.spl_registers import SPlRegisters

class Expression:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self):
        if self.operator == '+':
            return int(self.left ) + int(self.right)
        elif self.operator == '*':
            return int(self.left) * int(self.right)
        else:
            return int(self.left)

class LetCommandParser(SPlParser):
    def __init__(self, lexer):
        super().__init__(lexer)
        self.register_x = None
        self.register_y = None
        self.expression = None

    def parse(self):
        super().parse()
        self.register_x = self.current_token.value
        self.eat(REGISTER)

        self.eat(ASSIGN)

        self.parse_expression()

    def parse_expression(self):
        left, operator, right = None, None, None

        if self.current_token.type == REGISTER:
            left = SPlRegisters.read_reg(self.current_token.value)
            self.eat(REGISTER)
        else:
            left = self.current_token.value
            self.eat(INTEGER_CONST)

        if self.current_token.type == PLUS:
            operator = self.current_token.value
            self.eat(PLUS)
        elif self.current_token.type == MULTIPLY:
            operator = self.current_token.value
            self.eat(MULTIPLY)
        else:
            self.eat(EOL)

        if operator != None:
            if self.current_token.type == REGISTER:
                right = SPlRegisters.read_reg(self.current_token.value)
                self.eat(REGISTER)
            else:
                right = self.current_token.value
                self.eat(INTEGER_CONST)

        self.expression = Expression(left, operator, right)

    def evaluate(self):
        value = self.expression.evaluate()
        SPlRegisters.write_reg(self.register_x, value)
        return None