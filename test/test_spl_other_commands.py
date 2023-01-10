import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(project_root)

import src

test_path = os.path.dirname(__file__)

def test_print_command():
    sys.stdout = open('out.dat', 'w')

    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "print_command.txt"))
    pl_interpreter_obj.interpret_file()

    sys.stdout.close()
    with open('out.dat', 'r') as f:
        r5 = f.readline()
        assert r5.strip() == 'R5: 10'
        r6 = f.readline()
        assert r6.strip() == 'R6: 20'

    os.remove('out.dat')

def test_jump_command():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "jump_command.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R1") == 20

def test_call_return_command():
    pl_interpreter_obj = src.SPlInterpreter(
        os.path.join(test_path, "call_return_command.txt"))
    pl_interpreter_obj.interpret_file()

    assert src.SPlRegisters.read_reg("R6") == 4000
    assert src.SPlRegisters.read_reg("R7") == 5000

# def test_call_after_call_command():
#     pl_interpreter_obj = src.SPlInterpreter(
#         os.path.join(test_path, "call_after_call.txt"))
#     pl_interpreter_obj.interpret_file()
#
#     assert src.SPlRegisters.read_reg("R6") == 6000
#     assert src.SPlRegisters.read_reg("R7") == 7000
#     assert src.SPlRegisters.read_reg("R8") == 8000

# def test_call_inside_call_command():
#     pl_interpreter_obj = src.SPlInterpreter(
#         os.path.join(test_path, "call_inside_call.txt"))
#     pl_interpreter_obj.interpret_file()
#
#     assert src.SPlRegisters.read_reg("R6") == 4000
#     assert src.SPlRegisters.read_reg("R7") == 5000
#     assert src.SPlRegisters.read_reg("R8") == 8000