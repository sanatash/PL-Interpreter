from src.spl_parser import SPlParser
from src.spl_token import *
from src.spl_registers import SPlRegisters

class PrintCommandParser(SPlParser):
    def __init__(self, lexer):
        super().__init__(lexer)
        self.register_x = None

    def parse(self):
        self.register_x = self.current_token.value
        self.eat(REGISTER)

    def evaluate(self):
        rx = SPlRegisters.read_reg(self.register_x)
        if rx != None:
            print(f"{self.register_x}: {rx}")
        else:
            raise Exception('Cannot print the value of register, register not initialized!')

        return None