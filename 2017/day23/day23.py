import re
from collections import defaultdict
from dataclasses import dataclass

instr_with_digit = re.compile(r"(\w+) (\w) (-?\d+)")
instr_with_1_digit = re.compile(r"(\w+) (-?\d+)")
instr_with_2_digit = re.compile(r"(\w+) (-?\d+) (-?\d+)")
instr_with_2_reg = re.compile(r"(\w+) (\w) (\w)")
instr_with_1_reg = re.compile(r"(\w+) (\w)")

def parse_instruction(string: str) -> tuple[str, int]:
    matches = re.findall(instr_with_2_digit, string)
    if matches:
        match = list(matches[0])
        match[1] = int(match[1])
        match[2] = int(match[2])
        return tuple(match)
    matches = re.findall(instr_with_digit, string)
    if matches:
        match = list(matches[0])
        match[2] = int(match[2])
        return tuple(match)
    matches = re.findall(instr_with_1_digit, string)
    if matches:
        match = list(matches[0])
        match[1] = int(match[1])
        return tuple(match)
    matches = re.findall(instr_with_2_reg, string)
    if matches:
        return matches[0]
    matches = re.findall(instr_with_1_reg, string)
    if matches:
        return matches[0]
    raise Exception("unable to find matching")

with open("day23/day23.txt") as f:
    instructions = [parse_instruction(line) for line in f.readlines()]

@dataclass
class RegisterInfo:
    val: int
    last_sound: int

def new_reg_info():
    return RegisterInfo(0, 0)

class Program:
    registers: defaultdict[str, RegisterInfo]
    mul_count: int
    index: int

    def __init__(self):
        self.registers = defaultdict(new_reg_info)
        self.index = 0
        self.mul_count = 0

    def set_f(self, reg: str, val: (str | int)):
        if isinstance(val, int):
            self.registers[reg].val = val
        else:
            self.registers[reg].val = self.registers[val].val

    def sub(self, reg: str, val: (str | int)):
        if isinstance(val, int):
            self.registers[reg].val -= val
        else:
            self.registers[reg].val -= self.registers[val].val

    def mul(self, reg: str, val: (str | int)):
        self.mul_count += 1
        if isinstance(val, int):
            self.registers[reg].val *= val
        else:
            self.registers[reg].val *= self.registers[val].val

    def jump(self, reg: str, val: (str| int)):
        if (isinstance(reg, int) and reg != 0) or (not isinstance(reg, int) and self.registers[reg].val != 0):
            # jump
            if isinstance(val, int):
                return val
            return self.registers[reg].val
        return 1

    def run(self):
        jump_val = None
        count = 0
        while self.index >= 0 and self.index < len(instructions):
            match instructions[self.index][0]:
                case "set":
                    self.set_f(instructions[self.index][1], instructions[self.index][2])
                case "sub":
                    self.sub(instructions[self.index][1], instructions[self.index][2])
                case "mul":
                    self.mul(instructions[self.index][1], instructions[self.index][2])
                case "jnz":
                    jump_val = self.jump(instructions[self.index][1], instructions[self.index][2])
                case _:
                    break
            if jump_val:
                self.index += jump_val
                jump_val = None
            else:
                self.index += 1
            count += 1

print("----------PART 1----------")

prog = Program()
prog.run()
print(prog.mul_count)

print("----------PART 2----------")
b,c,h = 108400,110100,0
import math

def is_prime(number):
    """
    Checks if a number is prime.

    Args:
        number: An integer.

    Returns:
        True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

c = 110100
b = 108400
h = 0

for i in range(1001):
    if not is_prime(b):
        h += 1
    b += 17

print(h)
