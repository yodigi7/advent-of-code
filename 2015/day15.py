from copy import deepcopy
from dataclasses import dataclass
from math import perm


input = """Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
"""


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def permutations(items_count, max_teaspoons=100):
    ret_list = [[]]
    for _ in range(items_count - 1):
        new_ret_list = []
        for permutation in ret_list:
            for i in range(max_teaspoons - sum(permutation) + 1):
                copy = permutation[:]
                copy.append(i)
                new_ret_list.append(copy)
            test = None
        ret_list = new_ret_list
    # Finish out permutations with last ingredient to get to 100
    new_ret_list = []
    for permutation in ret_list:
        copy = permutation[:]
        copy.append(max_teaspoons - sum(permutation))
        new_ret_list.append(copy)
    ret_list = new_ret_list
    return ret_list


ingredients = []


def get_ingredients():
    for line in input.splitlines():
        words = line.split()
        name = words[0][:-1]
        capacity, durability, flavor, texture = [
            int(words[x][:-1]) for x in (2, 4, 6, 8)
        ]
        calories = int(words[10])
        ingredients.append(
            Ingredient(name, capacity, durability, flavor, texture, calories)
        )


def calculate_score(ingredient_portions: list) -> int:
    capacity, durability, flavor, texture = [0] * 4
    for i, portion in enumerate(ingredient_portions):
        capacity += portion * ingredients[i].capacity
        durability += portion * ingredients[i].durability
        flavor += portion * ingredients[i].flavor
        texture += portion * ingredients[i].texture
    capacity = max(capacity, 0)
    durability = max(durability, 0)
    flavor = max(flavor, 0)
    texture = max(texture, 0)
    return capacity * durability * flavor * texture


def calories(ingredient_portions: list) -> int:
    return sum(
        portion * ingredients[i].calories
        for i, portion in enumerate(ingredient_portions)
    )


if __name__ == "__main__":
    get_ingredients()
    print(
        max(
            calculate_score(permutation)
            for permutation in permutations(len(ingredients))
        )
    )
    print(
        max(
            calculate_score(permutation)
            for permutation in permutations(len(ingredients))
            if calories(permutation) == 500
        )
    )
