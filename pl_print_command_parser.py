from pl_parser import PlParser
from pl_token import *
from pl_registers import PlRegisters

class PrintCommandParser(PlParser):
    def __init__(self, lexer):
        super().__init__(lexer)
        self.register_x = None

    def parse(self):
        self.register_x = self.current_token.value
        self.eat(REGISTER)

    def evaluate(self):
        rx = PlRegisters.read_reg(self.register_x)
        if rx != None:
            print(f"{self.register_x}: {rx}")
        else:
            raise Exception('Cannot print the value of register, register not initialized!')

        return None