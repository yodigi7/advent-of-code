# https://www.redblobgames.com/grids/hexagons/
# with open("day11/day11test.txt") as f:
with open("day11/day11.txt") as f:
    input = f.readline().split(",")

print("----------PART 1----------")
# going to try the trick of using complex numbers for coords
coords = 0+0j
def move(dir: str, coords: complex):
    match dir:
        case "n":
            coords += -1j
        case "s":
            coords += 1j
        case "nw":
            if coords.real % 2 != 0:
                coords += -1j
            coords += -1
        case "ne":
            if coords.real % 2 != 0:
                coords += -1j
            coords += 1
        case "sw":
            if coords.real % 2 == 0:
                coords += 1j
            coords -= 1
        case "se":
            if coords.real % 2 == 0:
                coords += 1j
            coords += 1
    return coords

def get_distance(coords: complex) -> int:
    count = 0
    while coords.imag != 0:
        if coords.imag < 0 and coords.real < 0:
            dir = "se"
        elif coords.imag < 0 and coords.real > 0:
            dir = "sw"
        elif coords.imag > 0 and coords.real > 0:
            dir = "nw"
        elif coords.imag > 0 and coords.real < 0:
            dir = "ne"
        elif coords.real == 0 and coords.imag < 0:
            dir = "s"
        elif coords.real == 0 and coords.imag > 0:
            dir = "n"
        coords = move(dir, coords)
        count += 1
    return count

max_dist = 0
skip = 0
for dir in input:
    skip -= 1
    coords = move(dir, coords)
    if skip <= 0:
        dist = get_distance(coords)
        max_dist = max(max_dist, dist)
        skip = max(0, max_dist - dist)


print(get_distance(coords))

# not 1058 too low
print("----------PART 2----------")
print(max_dist)