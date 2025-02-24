from functools import reduce

with open("day10/day10.txt") as f:
    input = [int(x) for x in f.readline().split(",")]

list_len = 256

def hash(lst: list[int], pos: int, length: int) -> list[int]:
    global list_len
    ret_list = lst[:]
    first_segment = []
    second_segment = []
    for i in range(list_len):
        if i < length:
            first_segment.append(lst[(pos + i)%list_len])
        else:
            second_segment.append(lst[(pos + i)%list_len])
    first_segment.reverse()
    for i in range(list_len):
        if i < length:
            ret_list[(pos + i)%list_len] = first_segment.pop(0)
        else:
            ret_list[(pos + i)%list_len] = second_segment.pop(0)
    return ret_list

def full_hash(lst: list[int], lengths: list[int]) -> list[int]:
    curr_pos = 0
    skip = 0
    for length in [x for x in lengths]:
        lst = hash(lst, curr_pos, length)
        curr_pos += length + skip
        curr_pos %= list_len
        skip += 1
    return lst

# Could do in place but don't feel like it
print("----------PART 1----------")
curr_list = [i for i in range(list_len)]
curr_list = full_hash(curr_list, input)

print(curr_list[0]*curr_list[1])

print("----------PART 2----------")
with open("day10/day10.txt") as f:
    input = [ord(x) for x in f.readline()]

input.extend([17, 31, 73, 47, 23])
curr_list = [i for i in range(list_len)]
curr_pos = 0
skip = 0
for _ in range(64):
    for i, length in enumerate(input):
        curr_list = hash(curr_list, curr_pos, length)

        curr_pos += length + skip
        curr_pos %= list_len
        skip += 1

def to_dense_hash(sparse_hash: list[int]) -> list[int]:
    return [reduce(lambda x, y: x^y, sparse_hash[i*16:(i+1)*16]) for i in range(16)]

dense_hash = to_dense_hash(curr_list)

def to_hex(num: int) -> str:
    return f"{hex(num)[2:].zfill(2)}"

hexs = [to_hex(num) for num in dense_hash]
print(''.join(hexs))
