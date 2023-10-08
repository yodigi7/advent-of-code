import math
if __name__ == "__main__":
    # with open("test.txt", "r") as f:
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
        print(digit_line)

    def solve(partial_solution, best_solve):
        curr_pos = partial_solution[-1]
        visited_coords = set(partial_solution)
        if curr_pos == end_coord:
            return 0
        if best_solve < 0:
            return math.inf
        potential_moves = []
        if curr_pos[0] - 1 >= 0 and (curr_pos[0] - 1, curr_pos[1]) not in visited_coords:
            potential_moves.append((curr_pos[0] - 1, curr_pos[1]))
        if curr_pos[0] + 1 < len(grid) and (curr_pos[0] + 1, curr_pos[1]) not in visited_coords:
            potential_moves.append((curr_pos[0] + 1, curr_pos[1]))
        if curr_pos[1] - 1 >= 0 and (curr_pos[0], curr_pos[1] - 1) not in visited_coords:
            potential_moves.append((curr_pos[0], curr_pos[1] - 1))
        if curr_pos[1] + 1 < len(grid[0]) and (curr_pos[0], curr_pos[1] + 1) not in visited_coords:
            potential_moves.append((curr_pos[0], curr_pos[1] + 1))

        curr_best_solve = math.inf
        current_elevation = num_grid[curr_pos[0]][curr_pos[1]]
        for move in potential_moves:
            # Climb up max 1 level
            next_elevation = num_grid[move[0]][move[1]]
            if next_elevation <= current_elevation + 1 and next_elevation >= current_elevation:
                # decrement best_solve because we just used on move
                new_partial_solution = partial_solution[:]
                new_partial_solution.append(move)
                curr_best_solve = min(curr_best_solve, 1 + solve(new_partial_solution, best_solve - 1))
        # if curr_best_solve < math.inf:
        #     print(curr_best_solve)
        return curr_best_solve

    print(solve([start_coord], math.inf))
