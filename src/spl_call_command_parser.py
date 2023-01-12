from src.spl_parser import SPlParser
from src.spl_token import *

class CallCommandParser(SPlParser):
    def __init__(self, lexer):
        super().__init__(lexer)
        self.goto_label = None

    def parse(self):
        self.lexer.eat(COMMAND)
        self.goto_label = self.lexer.get_current_token().value
        self.lexer.eat(GOTO_LABEL)

    def evaluate(self):
        return self.goto_label