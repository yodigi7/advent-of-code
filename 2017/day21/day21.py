from typing import Tuple, Set, List
# from copy import deepcopy

def parse_rule(rule: str) -> tuple[tuple[tuple[str]], tuple[tuple[str]]]:
    input, output = rule.split(" => ")
    return tuple(tuple(c) for c in input.split("/")), tuple(tuple(c) for c in output.split("/"))

with open("day21/day21.txt") as f:
    rules = [parse_rule(rule.strip()) for rule in f.readlines()]

def rotate_90(matrix: Tuple[Tuple[str, ...], ...]) -> Tuple[Tuple[str, ...], ...]:
    return tuple(zip(*matrix[::-1]))

def flip_vertical(matrix: Tuple[Tuple[str, ...], ...]) -> Tuple[Tuple[str, ...], ...]:
    return tuple(matrix[::-1])

def all_rot_options(matrix: Tuple[Tuple[str, ...], ...]) -> Set[Tuple[Tuple[str, ...], ...]]:
    ret = set()
    temp = rotate_90(matrix)
    ret.add(temp)
    temp = rotate_90(temp)
    ret.add(temp)
    temp = rotate_90(temp)
    ret.add(temp)
    return ret

def all_options(matrix: Tuple[Tuple[str, ...], ...]) -> Set[Tuple[Tuple[str, ...], ...]]:
    ret = set()
    vert_flip = flip_vertical(matrix)
    for matrix in (matrix, vert_flip):
        ret.add(matrix)
        for opt in all_rot_options(matrix):
            ret.add(opt)
    return ret

rules_2d = {key: output for input, output in rules for key in all_options(input) if len(input) == 2}
rules_3d = {key: output for input, output in rules for key in all_options(input) if len(input) == 3}

def split_grid_size(grid: Tuple[Tuple[str, ...], ...], size: int):
    # new_grid = []
    # for j in range(len(grid) // size):
    #     line = []
    #     for i in range(len(grid) // size):
    #         segment = tuple(tuple(row[i*size:i*size+size]) for row in grid[j*size:j*size+size])
    #         line.append(segment)
    #     line = [tuple(tuple(row[i*size:i*size+size]) for row in grid[j*size:j*size+size]) for i in range(len(grid) // size)]
    #     new_grid.append(line)
    # return new_grid
    return [[tuple(tuple(row[i*size:i*size+size]) for row in grid[j*size:j*size+size]) for i in range(len(grid) // size)] for j in range(len(grid) // size)]

def split_grid(grid: Tuple[Tuple[str, ...], ...]) -> List[List[Tuple[Tuple[str, ...], ...]]]:
    if len(grid) % 2 == 0:
        return split_grid_size(grid, 2)
    elif len(grid) % 3 == 0:
        return split_grid_size(grid, 3)
    else:
        raise Exception("Invalid state")

def swap_grid(grid: List[List[Tuple[Tuple[str, ...], ...]]]) -> List[List[Tuple[Tuple[str, ...], ...]]]:
    global rules_2d, rules_3d
    swap_dict = rules_2d if len(grid[0][0]) % 2 == 0 else rules_3d
    new_grid = [[swap_dict[grid[i][j]] for j in range(len(grid[0]))] for i in range(len(grid))]
    # new_grid = deepcopy(grid)
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         new_grid[i][j] = swap_dict[grid[i][j]]
    return new_grid

def merge_grid(grid: List[List[Tuple[Tuple[str, ...], ...]]]) -> Tuple[Tuple[str, ...], ...]:
    size = len(grid[0][0])
    # new_grid = []
    # for i in range(len(grid)):
    #     for k in range(size):
    #         # line = []
    #         # for j in range(len(grid[0])):
    #         #     line.extend(grid[i][j][k])
    #         line = tuple(item for j in range(len(grid[0])) for item in grid[i][j][k])
    #         new_grid.append(tuple(line))
    # return tuple(new_grid)
    return tuple(tuple(item for j in range(len(grid[0])) for item in grid[i][j][k]) for i in range(len(grid)) for k in range(size))

def count_on(grid: Tuple[Tuple[str, ...], ...]) -> int:
    return sum(row.count("#") for row in grid)

print("----------PART 1----------")
grid = ((".", "#", "."), (".", ".", "#"), ("#", "#", "#"))
for i in range(5):
    grid = merge_grid(swap_grid(split_grid(grid)))
print(count_on(grid))

print("----------PART 2----------")
for i in range(18-5):
    grid = merge_grid(swap_grid(split_grid(grid)))
print(count_on(grid))

