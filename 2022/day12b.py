import math
if __name__ == "__main__":
    with open("day12.txt", "r") as f:
        lines = f.readlines()
    grid = []
    num_grid = []
    for i, line in enumerate(lines):
        line = line.strip()
        grid.append([*line])
        digit_line = []
        for j, c in enumerate(line):
            if c == "S":
                start_coord = i, j
                digit_line.append(0)
            elif c == "E":
                end_coord = i, j
                digit_line.append(25)
            else:
                digit_line.append(ord(c) - 97)
        num_grid.append(digit_line)
    graph = {}

    tries = []
    places_visited = set()
    places_visited.add(start_coord)

    for i, _ in enumerate(num_grid):
        for j, c in enumerate(num_grid[i]):
            potential_moves = []
            current_elevation = num_grid[i][j]
            if current_elevation == 0:
                tries.append(((i, j), 0))
                places_visited.add((i, j))
            if i - 1 >= 0 and num_grid[i - 1][j] - 1 <= current_elevation:
                potential_moves.append((i - 1, j))
            if i + 1 < len(grid) and num_grid[i + 1][j] - 1 <= current_elevation:
                potential_moves.append((i + 1, j))
            if j - 1 >= 0 and num_grid[i][j - 1] - 1 <= current_elevation:
                potential_moves.append((i, j - 1))
            if j + 1 < len(grid[0]) and num_grid[i][j + 1] - 1 <= current_elevation:
                potential_moves.append((i, j + 1))
            graph[(i, j)] = potential_moves


    while True:
        current_try = tries[0]
        tries = tries[1:]
        if current_try[0] == end_coord:
            print(current_try[1])
            break
        next_solutions = []
        for next_coord in graph[current_try[0]]:
            if next_coord in places_visited:
                continue
            places_visited.add(next_coord)
            next_solutions.append(( next_coord, current_try[1] + 1 ))
        tries.extend(next_solutions)