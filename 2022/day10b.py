if __name__ == "__main__":
    x = 1
    with open("day10.txt", "r") as f:
        instructions = [line.strip() for line in f.readlines()]
    # Get all instructions
    instructions_to_add = []
    for i, instruction in enumerate(instructions):
        if instruction == "noop":
            instructions_to_add.append(instruction)
        else:
            _, v = instruction.split()
            instructions_to_add.append(int(v))
    # Get register values calculated
    register_hist = []
    for instruction in instructions_to_add:
        if instruction == "noop":
            register_hist.append(x)
        else:
            register_hist.append(x)
            register_hist.append(x)
            x += instruction
    # Last updated value if addX since it would have just finished completing
    if instructions_to_add[-1] != "noop":
        register_hist.append(x)
    for j in range(6):
        line1 = []
        for i in range(j*40, (j*40)+40):
            # print(list(range(i%40 - 1, (i%40)+2)))
            # print(register_hist[i])
            # print(i)
            if register_hist[i] in range(i%40 - 1, (i%40)+2):
                # line1.append("██")
                line1.append("#")
            else:
                # line1.append("░░")
                line1.append(".")
        print("".join(line1))
