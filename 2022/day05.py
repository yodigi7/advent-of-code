from collections import deque

def read_crate_line(line):
    crates = []
    spacing = [ 1+(4*i) for i in range(9) ]
    for space in spacing:
        crates.append(line[space])
    return crates

def add_crates(crates, stacks):
    for i, crate in enumerate(crates):
        if crate != ' ':
            stacks[i].append(crate)

def execute_instruction(instruction, stacks):
    count, from_stack, to_stack = instruction
    from_stack -= 1
    to_stack -= 1
    for _ in range(count):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)

if __name__ == "__main__":
    # Read in the stacks
    stacks = tuple( deque() for _ in range(9) )
    with open('day05.txt', 'r') as inputfile:
        lines = inputfile.readlines()
        crate_lines = list(reversed(lines[:8]))
        for crate_line in crate_lines:
            crates = read_crate_line(crate_line)
            add_crates(crates, stacks)

        instruction_lines = lines[10:]
        instructions = []
        for instruction in instruction_lines:
            instruction = instruction.split()
            instruction = (instruction[1], instruction[3], instruction[5])
            instruction = (int(i) for i in instruction)
            execute_instruction(instruction, stacks)
    for stack in stacks:
        print(stack.pop())
