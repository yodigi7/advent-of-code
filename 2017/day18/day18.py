import re
from collections import defaultdict, deque
from dataclasses import dataclass

@dataclass
class RegisterInfo:
    val: int
    last_sound: int

def send(reg: str):
    registers[reg].last_sound = registers[reg].val

def set_f(reg: str, val: (str | int)):
    if isinstance(val, int):
        registers[reg].val = val
    else:
        registers[reg].val = registers[val].val

def add(reg: str, val: (str | int)):
    try:
        registers[reg].val += val
    except:
        registers[reg].val += registers[val].val

def mul(reg: str, val: (str | int)):
    try:
        registers[reg].val *= val
    except:
        registers[reg].val *= registers[val].val

def mod(reg: str, val: (str | int)):
    try:
        registers[reg].val %= val
    except:
        registers[reg].val %= registers[val].val

def receive(reg: str):
    if registers[reg].val != 0:
        return registers[reg].last_sound
    return None

def jump(reg: str, val: str):
    if registers[reg].val > 0:
        # jump
        if isinstance(val, int):
            return val
        return registers[val].val
    # no op
    return 1

def new_reg_info():
    return RegisterInfo(0, 0)

registers: dict[str, RegisterInfo] = defaultdict(new_reg_info)

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


with open("day18/day18.txt") as f:
    instructions = [parse_instruction(x) for x in f.readlines()]

print("----------PART 1----------")


index = 0
jump_val = None
while index >= 0 and index < len(instructions):
    # execute instruction
    match instructions[index][0]:
        case "snd":
            send(instructions[index][1])
        case "set":
            set_f(instructions[index][1], instructions[index][2])
        case "add":
            add(instructions[index][1], instructions[index][2])
        case "mul":
            mul(instructions[index][1], instructions[index][2])
        case "mod":
            mod(instructions[index][1], instructions[index][2])
        case "rcv":
            val = receive(instructions[index][1])
            if val:
                print(val)
                break
        case "jgz":
            jump_val = jump(instructions[index][1], instructions[index][2])
    if jump_val:
        index += jump_val
        jump_val = None
    else:
        index += 1

print("----------PART 2----------")

class Program:
    registers: defaultdict[str, RegisterInfo]
    send_queue: deque[int]
    rec_queue: deque[int]
    index: int

    def __init__(self, p: int):
        self.send_queue = deque()
        self.rec_queue = deque()
        self.registers = defaultdict(new_reg_info)
        self.registers["p"].val = p
        self.index = 0

    def send(self, val: (str | int)):
        # self.registers[reg].last_sound = self.registers[reg].val
        if isinstance(val, int):
            self.send_queue.append(val)
        else:
            self.send_queue.append(self.registers[val].val)

    def set_f(self, reg: str, val: (str | int)):
        if isinstance(val, int):
            self.registers[reg].val = val
        else:
            self.registers[reg].val = self.registers[val].val

    def add(self, reg: str, val: (str | int)):
        try:
            self.registers[reg].val += val
        except:
            self.registers[reg].val += self.registers[val].val

    def mul(self, reg: str, val: (str | int)):
        try:
            self.registers[reg].val *= val
        except:
            self.registers[reg].val *= self.registers[val].val

    def mod(self, reg: str, val: (str | int)):
        try:
            self.registers[reg].val %= val
        except:
            self.registers[reg].val %= self.registers[val].val

    def receive(self, reg: str) -> (bool | None):
        if len(self.rec_queue) == 0:
            return True
        self.registers[reg].val = self.rec_queue.popleft()

    def jump(self, reg: str, val: (str| int)):
        if (isinstance(reg, int) and reg > 0) or (not isinstance(reg, int) and self.registers[reg].val > 0):
            # jump
            if isinstance(val, int):
                return val
            return self.registers[reg].val
        return 1

    def run(self):
        jump_val = None
        while self.index >= 0 and self.index < len(instructions):
            match instructions[self.index][0]:
                case "snd":
                    self.send(instructions[self.index][1])
                case "set":
                    self.set_f(instructions[self.index][1], instructions[self.index][2])
                case "add":
                    self.add(instructions[self.index][1], instructions[self.index][2])
                case "mul":
                    self.mul(instructions[self.index][1], instructions[self.index][2])
                case "mod":
                    self.mod(instructions[self.index][1], instructions[self.index][2])
                case "rcv":
                    val = self.receive(instructions[self.index][1])
                    if val:
                        break
                case "jgz":
                    jump_val = self.jump(instructions[self.index][1], instructions[self.index][2])
                case _:
                    break
            if jump_val:
                self.index += jump_val
                jump_val = None
            else:
                self.index += 1

prog_0 = Program(0)
prog_1 = Program(1)
sends = 0
first = True
while len(prog_0.rec_queue) != 0 or len(prog_1.rec_queue) != 0 or first:
    first = False
    prog_0.run()
    prog_1.run()
    prog_0.rec_queue.extend(prog_1.send_queue)
    prog_1.rec_queue.extend(prog_0.send_queue)
    sends += len(prog_1.send_queue)
    prog_0.send_queue = deque()
    prog_1.send_queue = deque()
print(sends)
