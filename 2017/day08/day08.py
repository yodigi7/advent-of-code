from collections import defaultdict
from dataclasses import dataclass
import re

max_val = 0

print("----------PART 1----------")
registers = defaultdict(int)
reg = re.compile(r"(\w+) (inc|dec) (-?\d+) (.*)")
cond_reg = re.compile(r"if (\w+) (.+) (-?\d+)")

@dataclass
class Conditional:
    register: str
    operation: str
    value: int

    def evaluate(self) -> bool:
        return eval(f"{registers[self.register]}{self.operation}{self.value}")

@dataclass
class Instruction:
    register: str
    operation: str
    operator: int
    conditional: Conditional

    def execute(self):
        global max_val
        match self.operation:
            case "dec":
                registers[self.register] -= self.operator
                max_val = max(registers[self.register], max_val)
            case "inc":
                registers[self.register] += self.operator
                max_val = max(registers[self.register], max_val)

def to_conditional(string: str) -> Conditional:
    matches = re.match(cond_reg, string)
    return Conditional(matches[1], matches[2], int(matches[3]))

def to_instruction(line: str) -> Instruction:
    matches = re.match(reg, line)
    return Instruction(matches[1], matches[2], int(matches[3]), to_conditional(matches[4]))

with open("day08/day08.txt") as f:
    instructions = [to_instruction(x.strip()) for x in f.readlines()]

for instruction in instructions:
    if instruction.conditional.evaluate():
        instruction.execute()
print(max(registers.values()))

print("----------PART 2----------")
print(max_val)