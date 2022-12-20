from pl_parser import PlParser
from pl_token import *

class ReturnCommandParser(PlParser):
    def __init__(self, lexer):
        super().__init__(lexer)

    def parse(self):
        self.goto_label = self.current_token.value
        # self.eat(GOTO_LABEL)

    def evaluate(self):
        return None