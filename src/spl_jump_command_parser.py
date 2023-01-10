from src.spl_parser import SPlParser
from src.spl_token import *

class JumpCommandParser(SPlParser):
    def __init__(self, lexer):
        super().__init__(lexer)
        self.goto_label = None

    def parse(self):
        self.goto_label = self.current_token.value
        self.eat(GOTO_LABEL)

    def evaluate(self):
        return self.goto_label