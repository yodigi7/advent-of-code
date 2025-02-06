def has_solution(target: int, operands: int) -> bool:
    if len(operands) == 1:
        return operands[0] == target
    if has_solution(target - operands[0], operands[1:]):
        return True
    if target % operands[0] == 0 and has_solution(target // operands[0], operands[1:]):
        return True
    return False

if __name__ == "__main__":
    count = 0
    with open('day07.txt', 'r') as inputfile:
        for line in inputfile.readlines():
            target, remaining = line.split(":")
            target = int(target)
            # Remove first because of leading space and reverse to work recursively correctly
            operands = [int(x) for x in remaining.split(" ")[1:][::-1]]
            if has_solution(target, operands):
                count += target
    print(count)