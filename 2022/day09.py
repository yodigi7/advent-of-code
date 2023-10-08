def update_t(h_coord, t_coord):
    if h_coord[1] - t_coord[1] == 2:
        t_coord = (h_coord[0], t_coord[1] + 1)
    elif h_coord[1] - t_coord[1] == -2:
        t_coord = (h_coord[0], t_coord[1] - 1)
    if h_coord[0] - t_coord[0] == 2:
        t_coord = (t_coord[0] + 1, h_coord[1])
    elif h_coord[0] - t_coord[0] == -2:
        t_coord = (t_coord[0] - 1, h_coord[1])
    return t_coord

if __name__ == "__main__":
    coords_visited = set()
    t_coord = (0, 0)
    h_coord = (0, 0)
    with open("day09.txt", "r") as f:
        instructions = [ line.split() for line in f.readlines() ]
        instructions = [(x[0], int(x[1])) for x in instructions]
    for direction, num in instructions:
        for _ in range(num):
            if direction == "R":
                h_coord = (h_coord[0]+1, h_coord[1])
            elif direction == "L":
                h_coord = (h_coord[0]-1, h_coord[1])
            elif direction == "U":
                h_coord = (h_coord[0], h_coord[1]-1)
            elif direction == "D":
                h_coord = (h_coord[0], h_coord[1]+1)
            t_coord = update_t(h_coord, t_coord)
            coords_visited.add(t_coord)
    print(len(coords_visited))
