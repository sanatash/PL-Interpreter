import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(project_root)

import src

test_path = os.path.dirname(__file__)

def test_let_expr_plus_operator():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "let_expr_plus.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R5") == 5

def test_let_expr_multiply_operator():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "let_expr_multiply.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R2") == 20

def test_let_expr_with_positive_numbers():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "let_expr_positive_numbers.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R9") == 48
    assert src.SPlRegisters.read_reg("R8") == 58
    assert src.SPlRegisters.read_reg("R7") == 42
    assert src.SPlRegisters.read_reg("R6") == 420
    assert src.SPlRegisters.read_reg("R5") == 840

def test_let_expr_with_negative_numbers():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "let_expr_negative_numbers.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R1") == 5
    assert src.SPlRegisters.read_reg("R2") == -2
    assert src.SPlRegisters.read_reg("R3") == -6
    assert src.SPlRegisters.read_reg("R4") == -100
    assert src.SPlRegisters.read_reg("R5") == 100