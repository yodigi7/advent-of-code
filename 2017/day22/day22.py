with open("day22/day22.txt") as f:
    input = [list(x.strip()) for x in f.readlines()]

def turn_left(direction: complex) -> complex:
    match direction:
        case -1:
            return -1j
        case 1:
            return 1j
        case -1j:
            return 1
        case 1j:
            return -1
        case _:
            raise Exception("Invalid direction")

def turn_right(direction: complex) -> complex:
    return turn_left(turn_left(turn_left(direction)))

def reverse(direction: complex) -> complex:
    return turn_left(turn_left(direction))

print("----------PART 1----------")
infected_coords = set(i+(j*1j) for i in range(len(input)) for j in range(len(input[0])) if input[i][j] == "#")
coord = (len(input) // 2) + ((len(input[0])//2)*1j)
direction = -1
infections = 0
for i in range(10_000):
    if coord in infected_coords:
        direction = turn_right(direction)
        infected_coords.remove(coord)
    else:
        direction = turn_left(direction)
        infected_coords.add(coord)
        infections += 1
    coord += direction
print(infections)

print("----------PART 2----------")
infected_coords = set(i+(j*1j) for i in range(len(input)) for j in range(len(input[0])) if input[i][j] == "#")
weakened_coords = set()
flagged_coords = set()

coord = (len(input) // 2) + ((len(input[0])//2)*1j)
direction = -1
infections = 0
for i in range(10_000_000):
    if coord in infected_coords:
        direction = turn_right(direction)
        infected_coords.remove(coord)
        flagged_coords.add(coord)
    elif coord in flagged_coords:
        direction = reverse(direction)
        flagged_coords.remove(coord)
    elif coord in weakened_coords:
        weakened_coords.remove(coord)
        infected_coords.add(coord)
        infections += 1
    else:
        direction = turn_left(direction)
        weakened_coords.add(coord)
    coord += direction
print(infections)