import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(project_root)

import src

test_path = os.path.dirname(__file__)

import src


def let_expr_plus_operator():
    pl_interpreter_obj = src.pl_interpreter.SPlInterpreter("D:\\Anat\\PycharmProjects\\ALPLInterpreter\\test\\let_expr_plus.txt")
    pl_interpreter_obj.interpret_file()

    assert src.pl_registers.SPlRegisters.read_reg("R5") == 5

def let_expr_multiply_operator():
    pl_interpreter_obj = src.pl_interpreter.SPlInterpreter(
        "D:\\Anat\\PycharmProjects\\ALPLInterpreter\\test\\let_expr_multiply.txt")
    pl_interpreter_obj.interpret_file()

    assert src.pl_registers.SPlRegisters.read_reg("R2") == 20

def let_expr_with_negative_numbers():
    pl_interpreter_obj = src.SPlInterpreter("/test/let_expr_negative_numbers.txt")
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R1") == 5
    assert src.SPlRegisters.read_reg("R2") == -2
    assert src.SPlRegisters.read_reg("R3") == -6




def if_equal_operator():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "if_equal_operator.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R3") == 9
    assert src.SPlRegisters.read_reg("R4") == 14

if __name__ == "__main__":
    if_equal_operator()