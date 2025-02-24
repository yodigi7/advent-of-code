from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass

with open("day24/day24.txt") as f:
    parts = [tuple(int(i) for i in x.strip().split("/")) for x in f.readlines()]

part_set = set()
for part in parts:
    if part in part_set:
        print("ERROR")
        print(part)
        continue
    part_set.add(part)

part_dict = defaultdict(set)

for part in parts:
    part_dict[part[0]].add(part)
    part_dict[part[1]].add(part)

@dataclass
class Bridge:
    parts: tuple[tuple[int]]
    required_connector: int

    def get_strength(self):
        return sum(sum(part) for part in self.parts)

    def copy(self):
        return Bridge(self.parts, self.required_connector)

def get_strongest_bridge(bridge: Bridge) -> Bridge:
    global part_dict
    best_bridge = bridge
    best_score = 0
    for part in part_dict[bridge.required_connector]:
        if part in bridge.parts:
            continue
        test_bridge = Bridge(bridge.parts + (part,), part[1] if bridge.required_connector == part[0] else part[0])
        test_bridge = get_strongest_bridge(test_bridge)
        test_bridge_score = test_bridge.get_strength()
        if test_bridge_score > best_score:
            best_bridge = test_bridge
            best_score = test_bridge_score
    return best_bridge

def get_longest_bridge(bridge: Bridge) -> Bridge:
    global part_dict
    best_bridge = bridge
    best_score = 0
    for part in part_dict[bridge.required_connector]:
        if part in bridge.parts:
            continue
        test_bridge = Bridge(bridge.parts + (part,), part[1] if bridge.required_connector == part[0] else part[0])
        test_bridge = get_longest_bridge(test_bridge)
        test_bridge_score = len(test_bridge.parts)
        if test_bridge_score > best_score:
            best_bridge = test_bridge
            best_score = test_bridge_score
        elif test_bridge_score == best_score and test_bridge.get_strength() > best_bridge.get_strength():
            best_bridge = test_bridge
    return best_bridge

print("----------PART 1----------")
bridge = get_strongest_bridge(Bridge((), 0))
print(bridge.get_strength())

print("----------PART 2----------")
bridge = get_longest_bridge(Bridge((), 0))
print(bridge.get_strength())