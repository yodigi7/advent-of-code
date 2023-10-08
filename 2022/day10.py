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
    # Print last updated value if addX since it would have just finished completing
    if instructions_to_add[-1] != "noop":
        register_hist.append(x)
    # Calculate answer
    ans = 0
    for i, register in enumerate(register_hist[19:220:40]):
        signal = (i*40+20)*register
        ans += signal
    print(ans)