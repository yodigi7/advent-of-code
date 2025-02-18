from typing import Set
from functools import lru_cache, cache, reduce
import math

def get_factors(num: int) -> Set[int]:
    small_factors = { x for x in range(1, math.ceil(math.sqrt(num))) if num % x == 0 }
    large_factors = { num/x for x in small_factors }
    return small_factors.union(large_factors)

def get_score(num: int) -> int:
    return sum(factor for factor in get_factors(num)) * 10

def get_score_2(num) -> int:
    return sum(factor for factor in get_factors(num) if factor * 50 <= num) * 11

def get_primes():
    primes = []
    i = 1
    while True:
        i += 1
        for prime in primes:
            if i % prime == 0:
                break
        else:
            yield i
            primes.append(i)


target = 34_000_000

test = 510510
# print(get_factors(test))
# print(f"test: {test}, score: {get_score(get_factors(test))}")

# print("------------PART 1------------")
# # Most efficient numbers since they are highly composite
# start = 0
# max_check = 0
# primes = []
# for prime in get_primes():
#     primes.append(prime)
#     house = reduce(lambda a, b: a*b, primes)
#     score = get_score(house)
#     # print(f"primes: {primes}, score: {score}, house: {house}")
#     start = max_check
#     max_check = house
#     if score >= target:
#         # print(f"primes: {primes}, score: {score}, house: {house}")
#         break

# print(f"start: {start}, max_check: {max_check}")
# for i in range(start, max_check):
#     score = get_score(i)
#     if i % 10000 == 0:
#         print(f"score: {score}, i: {i}")
#     if score >= target:
#         print("-----------------FINAL-----------------")
#         print(f"score: {score}, i: {i}")
#         print(i)
#         start = i
#         break


print("------------PART 2------------")
# Less than 4989600
# Most efficient numbers since they are highly composite
# start_2 = 0
# max_check = 0
# primes = []
# for prime in get_primes():
#     primes.append(prime)
#     house = reduce(lambda a, b: a*b, primes)
#     score = get_score_2(house)
#     # print(f"primes: {primes}, score: {score}, house: {house}")
#     start_2 = max_check
#     max_check = house
#     if score >= target:
#         # print(f"primes: {primes}, score: {score}, house: {house}")
#         break

# start_2 = max(start_2, i)
# print(f"start: {start_2}, max_check: {max_check}")
# for i in range(start_2, max_check):
#     score = get_score_2(i)
#     if i % 10000 == 0:
#         print(f"score: {score}, i: {i}")
#     if score >= target:
#         print("-----------------FINAL-----------------")
#         print(f"score: {score}, i: {i}")
#         print(i)
#         break


import numpy as np

BIG_NUM = 1000000  # try larger numbers until solution found

houses_a = np.zeros(BIG_NUM)
houses_b = np.zeros(BIG_NUM)

for elf in range(1, BIG_NUM):
    # houses_a[elf::elf] += 10 * elf
    houses_b[elf:(elf+1)*50:elf] += 11 * elf

# print(np.nonzero(houses_a >= target)[0][0])
print(np.nonzero(houses_b >= target)[0][0])