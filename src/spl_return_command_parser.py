from src.spl_parser import SPlParser


class ReturnCommandParser(SPlParser):
    def __init__(self, lexer):
        super().__init__(lexer)

    def parse(self):
        self.goto_label = self.lexer.get_current_token().value
        # self.eat(GOTO_LABEL)

    def evaluate(self):
        return None