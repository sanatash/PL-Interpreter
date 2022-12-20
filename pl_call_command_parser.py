from pl_parser import PlParser
from pl_token import *

class CallCommandParser(PlParser):
    def __init__(self, lexer):
        super().__init__(lexer)
        self.goto_label = None

    def parse(self):
        self.goto_label = self.current_token.value
        self.eat(GOTO_LABEL)

    def evaluate(self):
        return self.goto_label