from collections import defaultdict
import re

reg1 = re.compile(r"(\d+)(.*)")
reg2 = re.compile(r"(\d+)")
graph = defaultdict(set)
with open("day12/day12.txt") as f:
    input = f.readlines()
for line in input:
    matches = re.match(reg1, line)
    children = re.findall(reg2, matches[2])
    graph[matches[1]] = graph[matches[1]].union(set(children))
    for child in children:
        graph[child].add(matches[1])

print("----------PART 1----------")
def get_group(root: str) -> set[str]:
    global graph
    to_visit = [root]
    visited = set()
    while len(to_visit) > 0:
        item = to_visit.pop()
        if item in visited:
            continue
        visited.add(item)
        to_visit.extend(list(graph[item]))
    return visited
print(len(get_group("0")))

print("----------PART 2----------")
group_count = 0
visited = set()
for key in graph:
    if key in visited:
        continue
    visited = visited.union(get_group(key))
    group_count += 1
print(group_count)
