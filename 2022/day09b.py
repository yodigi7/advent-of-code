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
    # TODO: figure out why it is giving wrong answer only for my problem set, working for examples
    coords_visited = set()
    t_coord = (0, 0)
    coord_1 = (0, 0)
    coord_2 = (0, 0)
    coord_3 = (0, 0)
    coord_4 = (0, 0)
    coord_5 = (0, 0)
    coord_6 = (0, 0)
    coord_7 = (0, 0)
    coord_8 = (0, 0)
    h_coord = (0, 0)
    with open("day09.txt", "r") as f:
        instructions = [ line.split() for line in f.readlines() ]
        instructions = [(x[0], int(x[1])) for x in instructions]
    print(instructions)
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
            coord_1 = update_t(h_coord, coord_1)
            coord_2 = update_t(coord_1, coord_2)
            coord_3 = update_t(coord_2, coord_3)
            coord_4 = update_t(coord_3, coord_4)
            coord_5 = update_t(coord_4, coord_5)
            coord_6 = update_t(coord_5, coord_6)
            coord_7 = update_t(coord_6, coord_7)
            coord_8 = update_t(coord_7, coord_8)
            t_coord = update_t(coord_8, t_coord)
            coords_visited.add(t_coord)
    print(coords_visited)
    print(len(coords_visited))
