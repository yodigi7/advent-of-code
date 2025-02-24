from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Machine:
    tape: defaultdict[int, int]
    state: str
    index: int

    def __init__(self):
        self.tape = defaultdict(int)
        self.state = "a"
        self.index = 0

    def step(self):
        val = self.tape[self.index]
        match self.state:
            case "a":
                if val == 0:
                    self.tape[self.index] = 1
                    self.index += 1
                    self.state = "b"
                else:
                    self.tape[self.index] = 1
                    self.index -= 1
                    self.state = "e"
            case "b":
                if val == 0:
                    self.tape[self.index] = 1
                    self.index += 1
                    self.state = "c"
                else:
                    self.tape[self.index] = 1
                    self.index += 1
                    self.state = "f"
            case "c":
                if val == 0:
                    self.tape[self.index] = 1
                    self.index -= 1
                    self.state = "d"
                else:
                    self.tape[self.index] = 0
                    self.index += 1
                    self.state = "b"
            case "d":
                if val == 0:
                    self.tape[self.index] = 1
                    self.index += 1
                    self.state = "e"
                else:
                    self.tape[self.index] = 0
                    self.index -= 1
                    self.state = "c"
            case "e":
                if val == 0:
                    self.tape[self.index] = 1
                    self.index -= 1
                    self.state = "a"
                else:
                    self.tape[self.index] = 0
                    self.index += 1
                    self.state = "d"
            case "f":
                if val == 0:
                    self.tape[self.index] = 1
                    self.index += 1
                    self.state = "a"
                else:
                    self.tape[self.index] = 1
                    self.index += 1
                    self.state = "c"

print("----------PART 1----------")
m = Machine()
for i in range(12_523_873):
    m.step()
diagnostic_check = sum(m.tape.values())
print(diagnostic_check)

print("----------PART 2----------")
