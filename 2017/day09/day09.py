with open("day09/day09.txt") as f:
    input = f.readline()

# input = r"{{<!>},{<!>},{<!>},{<a>}}"
# input = r"{{<a>},{<a>},{<a>},{<a>}}"
# input = r"{{<ab>},{<ab>},{<ab>},{<ab>}}"
# input = r"{{{},{},{{}}}}"
# input = r"{{<a!>},{<a!>},{<a!>},{<ab>}}"
# input = r'<{o"i!a,<{i<a>'

def strip_exc(input: str) -> str:
    res = ""
    skip = False
    for char in input:
        if skip:
            skip = False
            continue
        if char == "!":
            skip = True
        else:
            res += char
    return res

def strip_garbage(input: str) -> str:
    res = ""
    garbage = False
    for char in input:
        if char == "<":
            garbage = True
        elif char == ">":
            garbage = False
        elif garbage == False:
            res += char
    return res

def calc_score(input: str) -> int:
    score = 0
    nested_level = 1
    for char in input:
        if char == "{":
            score += nested_level
            nested_level += 1
        if char == "}":
            nested_level -= 1
    return score

print("----------PART 1----------")
print(calc_score(strip_garbage(strip_exc(input))))


print("----------PART 2----------")
def count_garbage(input: str) -> int:
    count = 0
    garbage = False
    for char in input:
        if char == "<" and not garbage:
            garbage = True
        elif char == ">":
            garbage = False
        elif garbage == True:
            count += 1
    return count
print(count_garbage(strip_exc(input)))
