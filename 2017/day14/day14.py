from functools import reduce
from collections import deque

input = "amgozmfv"
# input = "flqrgnkx"

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

def full_hash(lst: list[int], lengths: list[int]) -> int:
    curr_pos = 0
    skip = 0
    for _ in range(64):
        for length in [x for x in lengths]:
            lst = hash(lst, curr_pos, length)
            curr_pos += length + skip
            curr_pos %= list_len
            skip += 1
    dense_hash = to_dense_hash(lst)
    hexes = [to_hex(num) for num in dense_hash]
    return "".join(hexes)

def to_dense_hash(sparse_hash: list[int]) -> list[int]:
    return [reduce(lambda x, y: x^y, sparse_hash[i*16:(i+1)*16]) for i in range(16)]

def to_hex(num: int) -> str:
    return f"{hex(num)[2:].zfill(2)}"

def hex_to_bin(num: str) -> str:
    return f"{bin(int(num, 16))[2:].zfill(4)}"

print("----------PART 1----------")
lengths2d = [[ord(x) for x in f"{input}-{i}"] for i in range(128)]
for i in lengths2d:
    i.extend([17, 31, 73, 47, 23])
disc = []
for i, lengths in enumerate(lengths2d):
    lst = [i for i in range(list_len)]
    hash_str = full_hash(lst, lengths)
    bin_hash = bin(int(hash_str, 16))[2:].zfill(128)
    disc.append(bin_hash)
answer = sum(x.count("1") for x in disc)
print(answer)

print("----------PART 2----------")

directions = (1, -1, 1j, -1j)
coords = [i+(j*1j) for i in range(len(disc)) for j in range(len(disc[0])) if disc[i][j] == "1"]
visited_coords = set()
remaining_coords = set(coords)
regions = 0
while True:
    if len(coords) == 0:
        break
    coord = coords.pop(0)
    if coord in visited_coords:
        continue
    to_check = deque((coord,))
    regions += 1
    while len(to_check) > 0:
        coord = to_check.popleft()
        if coord in visited_coords:
            continue
        visited_coords.add(coord)
        for dir in directions:
            next_coord = coord+dir
            if next_coord in coords and next_coord not in visited_coords:
                to_check.append(next_coord)
print(regions)
