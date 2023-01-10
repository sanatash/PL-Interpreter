
class SPlRegisters:

    register_dict = {"R0": None, "R1": None, "R2": None, "R3": None, "R4": None,
                     "R5": None, "R6": None, "R7": None, "R8": None, "R9": None}

    def __init__(self):
        pass

    @staticmethod
    def print_registers():
        print()
        print("All registers:")
        for i in range(0, 10):
            print(f"R{i}: {SPlRegisters.register_dict[str('R' + str(i))]}")

    @staticmethod
    def read_reg(reg):
        if SPlRegisters.register_dict[reg] != None:
            return SPlRegisters.register_dict[reg]
        else:
            raise Exception(f'Register {reg} is not defined!')

    @staticmethod
    def write_reg(reg, value):
        SPlRegisters.register_dict[reg] = value