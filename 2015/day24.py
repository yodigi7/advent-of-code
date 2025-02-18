from typing import List, Tuple
from functools import cache, reduce

@cache
def get_bucket_one(packages: Tuple[int], target: int) -> List[List[int]]:
    '''
    packages must be a reverse sorted list
    '''
    if target < 0:
        return []
    if target == 0:
        return [[]]
    options = []
    for i, package in enumerate(packages):
        if package > target:
            continue
        if package == target:
            return [[package]]
        packages_copy = packages[i+1:]
        option = get_bucket_one(packages_copy, target - package)
        if option:
            for answer in option:
                options.append([package, *answer])
    return options


def calc_qe(solution: List[int]) -> int:
    return reduce(lambda x, y: x*y, solution)


with open("day24.txt") as f:
    packages = sorted([int(x) for x in f.readlines()], reverse=True)

# target weight to put in each bucket
target_weight = sum(packages)//3

print("--------------PART 1--------------")
solutions = sorted(get_bucket_one(tuple(packages), target_weight), key=lambda x: len(x))
solutions_to_check = [x for x in solutions if len(x) == len(solutions[0])]
solution = sorted(solutions_to_check, key=calc_qe)
print(calc_qe(solution[0]))
print("--------------PART 2--------------")
# target weight to put in each bucket
target_weight = sum(packages)//4
solutions = sorted(get_bucket_one(tuple(packages), target_weight), key=lambda x: len(x))
solutions_to_check = [x for x in solutions if len(x) == len(solutions[0])]
solution = sorted(solutions_to_check, key=calc_qe)
print(calc_qe(solution[0]))