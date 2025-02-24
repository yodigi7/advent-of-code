with open("day13/day13.txt") as f:
    input = [[int(x) for x in line.strip().split(": ")] for line in f.readlines()]

def is_at_top(list_len: int, seconds: int) -> int:
    return seconds % (2*(list_len-1)) == 0

def get_severity(depth: int, range: int) -> int:
    return depth * range

print("----------PART 1----------")
severity = 0
for depth, range in input:
    if is_at_top(range, depth):
        severity += get_severity(depth, range)
        print(range, depth)
print(severity)

print("----------PART 2----------")
offset = 0
while True:
    for depth, range in input:
        if is_at_top(range, depth + offset):
            break
    else:
        break
    offset += 1
print(offset)
