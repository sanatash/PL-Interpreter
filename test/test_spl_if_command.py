import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(project_root)

import src

test_path = os.path.dirname(__file__)


def test_if_equal_operator():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "if_equal_operator.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R3") == 12
    assert src.SPlRegisters.read_reg("R4") == 14

def test_if_less_than_operator():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "if_less_than_operator.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R3") == 35

def test_if_greater_than_operator():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "if_greater_than_operator.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R3") == 45
