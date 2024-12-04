def compare(left, right):
    left = left
    right = right
    if left[0] == "[":
        left_list = extract_list(left)
    else:
        left_index = left.index(",")
        left_num = int(left[:left_index])
    if right[0] == "[":
        right_list = extract_list(right)
    else:
        right_index = right.index(",")
        right_num = int(right[:right_index])
    if left_list and right_list:
        # Ran out of both items
        if left == "" and right == "":
            # Continue looking
            return -1
        # Ran out of left items
        if left == "":
            return 1
        # Ran out of right items
        elif right == "":
            return 0
        if left_num < right_num:
            return 1
        elif left_num > right_num:
            return 0
        else:
            return compare(left[left_index+1:], right[right_index+1:])
    elif left_list and not right_list:
        # TODO
        pass
    elif not left_list and right_list:
        # TODO
        pass
    else:
        # TODO
        res = compare()


def extract_list(inp):
    brackets = 0
    for i, c in enumerate(inp):
        if c == "[":
            brackets += 1
        elif c == "]":
            brackets -= 1
            if brackets == 0:
                return inp[:i]
    raise Exception("not supposed to happen")

if __name__ == "__main__":
    with open("test.txt", "r") as f:
    # with open("day13.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    pairs = []
    pair = []
    for line in lines:
        if line == "":
            pairs.append(pair)
            pair = []
        else:
            pair.append(line)
    pairs.append(pair)

    indexes = []
    for i, pair in enumerate(pairs, start=1):
        print(pair)
        left, right = pair
        print(compare(left[1:], right[1:]))