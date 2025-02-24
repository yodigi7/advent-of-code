import re

def spin(lst: list[str], x: int) -> list[str]:
    first = lst[-x:]
    first.extend(lst[:-x])
    return first

def exchange(lst: list[str], x: int, y: int) -> list[str]:
    ret_lst = lst[:]
    ret_lst[x], ret_lst[y] = ret_lst[y], ret_lst[x]
    # print(f"ret list: {ret_lst}")
    return ret_lst

def partner(lst: list[str], a: str, b: str) -> list[str]:
    return exchange(lst, lst.index(a), lst.index(b))

regXY = re.compile(r"(\d+)/(\d+)")
def get_x_y(input: str) -> list[int]:
    return [int(x) for x in re.findall(regXY, input)[0]]

regAB = re.compile(r"(\w+)/(\w+)")
def get_a_b(input: str) -> list[str]:
    return re.findall(regAB, input)[0]

with open("day16/day16.txt") as f:
    moves = f.readline().split(',')

print("----------PART 1----------")
programs = list("abcdefghijklmnop")
for move in moves:
    match move[0]:
        case "s":
            # print(f"move: {move}")
            programs = spin(programs, int(move[1:]))
        case "x":
            # print(f"move: {move}")
            x, y = get_x_y(move)
            programs = exchange(programs, x, y)
        case "p":
            # print(f"move: {move}")
            a, b = get_a_b(move[1:])
            programs = partner(programs, a, b)
    # print(f"programs: {programs}")
print("".join(programs))

print("----------PART 2----------")
programs = list("abcdefghijklmnop")
programs_start = list("abcdefghijklmnop")

positions = []
for i in range(1_000_000_000 // len(moves)):
    programs_str = "".join(programs)
    if programs_str in positions:
        print(f"{"".join(positions[1_000_000_000 % len(positions)])}")
        break
    positions.append(programs_str)
    for move in moves:
        match move[0]:
            case "s":
                programs = spin(programs, int(move[1:]))
            case "x":
                x, y = get_x_y(move)
                programs = exchange(programs, x, y)
            case "p":
                a, b = get_a_b(move[1:])
                programs = partner(programs, a, b)
        programs_str = "".join(programs)
