from functools import cache
from itertools import combinations, permutations
import math


input = """11
30
47
31
32
36
3
1
5
3
32
36
15
11
46
26
28
1
19
3
"""


@cache
def get_possibilities(containers, target_size) -> list:
    if target_size <= 0:
        return []
    possibilities = []
    for i, container in enumerate(containers):
        if container < target_size:
            for possibility in get_possibilities(
                containers[i + 1 :], target_size=target_size - container
            ):
                possibility.insert(0, container)
                possibilities.append(possibility)
        elif container == target_size:
            possibilities.append([container])
    return possibilities


@cache
def num_possibilities(containers, target_size, container_count=math.inf):
    if target_size <= 0 or container_count == 0:
        return 0
    possibilities = 0
    for i, container in enumerate(containers):
        if container < target_size:
            possibilities += num_possibilities(
                containers[i + 1 :], target_size - container, container_count - 1
            )
        elif container == target_size:
            possibilities += 1
    return possibilities


if __name__ == "__main__":
    target_size = 150
    # Part 1
    containers = tuple(int(x) for x in input.splitlines())
    print(num_possibilities(containers, target_size=target_size))
    # Part 2
    print(
        num_possibilities(
            containers,
            target_size,
            len(
                min(
                    get_possibilities(containers, target_size=target_size),
                    key=len,
                )
            ),
        )
    )
