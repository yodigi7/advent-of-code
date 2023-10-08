def get_visible_trees(lst, reverse=False):
    lowest_tree = -1
    visible_trees = set()
    for i, tree in enumerate(lst):
        if tree > lowest_tree:
            lowest_tree = tree
            visible_trees.add(i)
    # Want to get the visible trees looking from both ways
    if reverse:
        visible_trees = visible_trees.union({len(lst) - i - 1 for i in get_visible_trees(reversed(lst), reverse=False)})
    return visible_trees

if __name__ == "__main__":
    temp = True
    grid = []
    row_visible_trees = set()
    column_visible_trees = set()
    with open("day08.txt", "r") as f:
        grid = [[int(x) for x in line.strip()] for line in f.readlines()]
    row_visible_trees = row_visible_trees.union({(i, tree) for i, row in enumerate(grid) for tree in get_visible_trees(row, reverse=True)})
    for i in range(len(grid[0])):
        column = [grid[j][i] for j in range(len(grid))]
        visible_trees = {(tree, i) for tree in get_visible_trees(column, reverse=True)}
        column_visible_trees = column_visible_trees.union(visible_trees)
    print(len(row_visible_trees.union(column_visible_trees)))
