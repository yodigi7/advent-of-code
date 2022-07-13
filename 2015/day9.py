from itertools import permutations
from collections import defaultdict
import math

input = """Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46
"""

paths = defaultdict(dict)


def add_path(string):
    split_str = string.split(" = ")
    dist = int(split_str[1])
    split_str = split_str[0]
    start, end = split_str.split(" to ")
    paths[start][end] = dist
    paths[end][start] = dist


if __name__ == "__main__":
    for line in input.splitlines():
        add_path(line)
    shortest_dist = math.inf
    shortest_path = None
    longest_dist = -math.inf
    longest_path = None
    for permutation in permutations(paths.keys()):
        dist = 0
        for start, end in zip(permutation[:-1], permutation[1:]):
            dist += paths[start][end]
        if dist < shortest_dist:
            shortest_dist = dist
            shortest_path = permutation
        if dist > longest_dist:
            longest_dist = dist
            longest_path = permutation
    print(f"Shortest dist: {shortest_dist}")
    print(f"Shortest path: {shortest_path}")
    print(f"Longest dist: {longest_dist}")
    print(f"Longest path: {longest_path}")
