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
        self.lexer.eat(COMMAND)
        self.register_x = self.lexer.get_current_token().value
        self.lexer.eat(REGISTER)

        self.lexer.eat(ASSIGN)

        self.parse_expression()

    def parse_expression(self):
        left, operator, right = None, None, None

        if self.lexer.get_current_token().type == REGISTER:
            left = SPlRegisters.read_reg(self.lexer.get_current_token().value)
            self.lexer.eat(REGISTER)
        else:
            left = self.lexer.get_current_token().value
            self.lexer.eat(INTEGER_CONST)

        if self.lexer.get_current_token().type == PLUS:
            operator = self.lexer.get_current_token().value
            self.lexer.eat(PLUS)
        elif self.lexer.get_current_token().type == MULTIPLY:
            operator = self.lexer.get_current_token().value
            self.lexer.eat(MULTIPLY)
        else:
            self.lexer.eat(EOL)

        if operator != None:
            if self.lexer.get_current_token().type == REGISTER:
                right = SPlRegisters.read_reg(self.lexer.get_current_token().value)
                self.lexer.eat(REGISTER)
            else:
                right = self.lexer.get_current_token().value
                self.lexer.eat(INTEGER_CONST)

        self.expression = Expression(left, operator, right)

    def evaluate(self):
        value = self.expression.evaluate()
        SPlRegisters.write_reg(self.register_x, value)
        return None