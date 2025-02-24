import string

with open("day19/day19.txt") as f:
    grid = [[x for x in line.strip("\n")] for line in f.readlines()]

for i in range(len(grid)):
    grid[i].insert(0, " ")
    grid[i].append(" ")

grid.insert(0, [" " for _ in range(len(grid[0]))])
grid.append([" " for _ in range(len(grid[0]))])

def find_start(grid: list[list[str]]) -> complex:
    return (grid[1].index("|") * 1j) + 1

def valid_coords(coords: complex, grid: list[list[str]]) -> bool:
    return grid[coords.real][coords.imag] not in (" ")

print("----------PART 1----------")
curr_coord = find_start(grid)
prev_coord = curr_coord
direction = 1
letters = []
steps = 0
while True:
    if grid[int(curr_coord.real)][int(curr_coord.imag)] == "+":
        # check for which direction to change
        for new_direction in (1, -1, 1j, -1j):
            next_coord = new_direction + curr_coord
            if next_coord == prev_coord or grid[int(next_coord.real)][int(next_coord.imag)] == " " or (int(next_coord.real) != int(curr_coord.real) and grid[int(next_coord.real)][int(next_coord.imag)] == "-") or (int(next_coord.imag) != int(curr_coord.imag) and grid[int(next_coord.real)][int(next_coord.imag)] == "|"):
                continue
            direction = new_direction
            break
        else:
            raise Exception("Cannot find next direction")
    elif grid[int(curr_coord.real)][int(curr_coord.imag)] in string.ascii_uppercase:
        letters.append(grid[int(curr_coord.real)][int(curr_coord.imag)])
    elif grid[int(curr_coord.real)][int(curr_coord.imag)] == " ":
        break
    curr_coord, prev_coord = curr_coord + direction, curr_coord
    steps += 1
print("".join(letters))

print("----------PART 2----------")
print(steps)
