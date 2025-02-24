with open("day05/day05.txt") as f:
    instructions = [int(line.strip()) for line in f.readlines()]
instructions2 = instructions[:]

print("----------PART 1----------")
idx = 0
steps = 0
try:
    while True:
        i = instructions[idx]
        instructions[idx] += 1
        idx += i
        steps += 1
except IndexError as e:
    print(steps)

print("----------PART 2----------")
idx = 0
steps = 0
try:
    while True:
        i = instructions2[idx]
        if i >= 3:
            instructions2[idx] -= 1
        else:
            instructions2[idx] += 1
        idx += i
        steps += 1
except IndexError as e:
    print(steps)