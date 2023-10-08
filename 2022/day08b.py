def get_visible_trees(tree_height, lst):
    for i, height in enumerate(lst):
        if height >= tree_height:
            return i + 1
    return len(lst)

def get_score(grid, x, y):
    tree_height = grid[y][x]
    trees_above = []
    trees_below = []
    trees_above = [grid[j][x] for j in reversed(range(y))]
    trees_below = [grid[j][x] for j in range(y+1, len(grid))]
    trees_left = list(reversed(grid[y][:x]))
    trees_right = grid[y][x+1:]
    return get_visible_trees(tree_height, trees_above) * get_visible_trees(tree_height, trees_below) * get_visible_trees(tree_height, trees_left) * get_visible_trees(tree_height, trees_right)


if __name__ == "__main__":
    temp = True
    grid = []
    row_visible_trees = set()
    column_visible_trees = set()
    with open("day08.txt", "r") as f:
        grid = [[int(x) for x in line.strip()] for line in f.readlines()]
    best_coord = max(((i, j) for i in range(1, len(grid[0])-1) for j in range(1, len(grid)-1)), key=lambda tup: get_score(grid, tup[0], tup[1]))
    print(get_score(grid, best_coord[0], best_coord[1]))
