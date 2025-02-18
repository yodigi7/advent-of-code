from functools import partial
from typing import Callable
import re

registers = {"a": 0, "b": 0}
instruction_ptr = 0

def hlf(reg: str):
    def hlf():
        global registers, instruction_ptr
        nonlocal reg
        registers[reg] //= 2
        instruction_ptr += 1
    return hlf

def tpl(reg: str):
    def tpl():
        global registers, instruction_ptr
        nonlocal reg
        registers[reg] *= 3
        instruction_ptr += 1
    return tpl

def inc(reg: str):
    def inc():
        global registers, instruction_ptr
        nonlocal reg
        registers[reg] += 1
        instruction_ptr += 1
    return inc

def jmp(offset: int):
    def jmp():
        global instruction_ptr
        nonlocal offset
        instruction_ptr += offset
    return jmp

def jie(offset: int, reg: str):
    def jie():
        global registers, instruction_ptr
        nonlocal offset, reg
        if registers[reg] % 2 == 0:
            instruction_ptr += offset
        else:
            instruction_ptr += 1
    return jie
def jio(offset: int, reg: str):
    def jio():
        global registers, instruction_ptr
        nonlocal offset, reg
        if registers[reg] == 1:
            instruction_ptr += offset
        else:
            instruction_ptr += 1
    return jio


single_arg_reg = re.compile(r"(\w+) ([a-zA-Z0-9-+]+)$")
double_arg_reg = re.compile(r"(\w+) (\w), ([+-]\d+)$")
def map_to_instr(line: str) -> Callable[[], None]:
    res = re.search(single_arg_reg, line)
    if res:
        match res[1]:
            case "hlf":
                return hlf(res[2])
            case "tpl":
                return tpl(res[2])
            case "inc":
                return inc(res[2])
            case "jmp":
                return jmp(int(res[2]))
            case _:
                raise Exception("Not matching on expected instructions")
    res = re.search(double_arg_reg, line)
    if not res:
        raise Exception("Not matching on either regex")
    match res[1]:
        case "jie":
            return jie(reg=res[2], offset=int(res[3]))
        case "jio":
            return jio(reg=res[2], offset=int(res[3]))
        case _:
            raise Exception("Not matching on expected instructions")


raw_instructions = []
# with open("day23test.txt") as f:
with open("day23.txt") as f:
    raw_instructions = f.readlines()
instructions = [map_to_instr(i) for i in raw_instructions]
print("-------------------PART 1-------------------")
while instruction_ptr >= 0 and instruction_ptr < len(instructions):
    instructions[instruction_ptr]()
print(registers["b"])
print("-------------------PART 2-------------------")
registers = {"a": 1, "b": 0}
instruction_ptr = 0
while instruction_ptr >= 0 and instruction_ptr < len(instructions):
    instructions[instruction_ptr]()
print(registers["b"])

