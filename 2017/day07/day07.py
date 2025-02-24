from typing import List, Tuple
import re

with open("day07/day07.txt") as f:
    lines = f.readlines()

reg1 = re.compile(r"(\w+) \(\d+\)( -> (\w+,? ?)+)?")
reg2 = re.compile(r"(\w+)")

print("----------PART 1----------")
def parse(line: str) -> List[Tuple[str]]:
    res = []
    matches = re.match(reg1, line)
    node = matches[1]
    res.append(node)
    children = []
    if matches[2]:
        children = re.findall(reg2, matches[2])
        res.append(tuple(children))
    else:
        res.append(tuple())
    return res

parsed_lines = [parse(line) for line in lines]
nodes = {line[0] for line in parsed_lines}
children = {child for line in parsed_lines for child in line[1]}
root = list(nodes.difference(children))[0]
print(root)


print("----------PART 2----------")
from dataclasses import dataclass

@dataclass
class Program:
    key: str = ""
    weight: int = 0
    children: List = list

    def get_weight(self) -> int:
        return sum(child.get_weight() for child in self.children) + self.weight

    def valid_weights(self) -> bool:
        weight = None
        valid = True
        for child in self.children:
            child.valid_weights()
            if not weight:
                weight = child.get_weight()
                continue
            if weight != child.get_weight():
                valid = False
        if not valid:
            print([child.key for child in self.children])
            print([child.get_weight() for child in self.children])
            print(self.key)
        return valid


reg1 = re.compile(r"(\w+) \((\d+)\)( -> (\w+,? ?)+)?")
def parse2(line: str) -> List[Tuple[str]]:
    res = []
    matches = re.match(reg1, line)
    node = matches[1]
    res.append(node)
    children = []
    weight = int(matches[2])
    res.append(weight)
    if matches[3]:
        children = re.findall(reg2, matches[3])
        res.append(tuple(children))
    else:
        res.append(tuple())
    return res

programs = dict()
for line in lines:
    key, weight, children = parse2(line)
    program_children = []
    for child in children:
        if child not in programs:
            programs[child] = Program(key=child)
        program_children.append(programs[child])
    if key not in programs:
        programs[key] = Program(key=key)
    programs[key].weight = weight
    programs[key].children = tuple(program_children)

# print(programs)
print(programs[root].valid_weights())

print(programs["eionkb"].weight)
print(programs["eionkb"].weight - (1784 - 1777))