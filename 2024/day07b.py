def append(val1: int, val2: int) -> int:
    '''
    Append in reverse since the original list is reversed
    '''
    return int(f"{val2}{val1}")

def get_values(operands: list) -> set:
    if len(operands) == 1:
        return {operands[0]}
    values = get_values(operands[1:])
    ret = set()
    for x in values:
        ret.add(operands[0] * x)
        ret.add(operands[0] + x)
        ret.add(append(operands[0], x))
    return ret

if __name__ == "__main__":
    count = 0
    with open('day07.txt', 'r') as inputfile:
        for line in inputfile.readlines():
            target, remaining = line.split(":")
            target = int(target)
            # Remove first because of leading space and reverse to work recursively correctly
            operands = [int(x) for x in remaining.split(" ")[1:][::-1]]
            if target in get_values(operands):
                count += target
    print(count)