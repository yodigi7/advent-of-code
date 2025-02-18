from dataclasses import dataclass
from itertools import combinations
import math


@dataclass
class Item:
    cost: int
    damage: int = 0
    armor: int = 0


@dataclass
class Player:
    armor: int
    damage: int
    hp: int = 100


weapons = [Item(cost=8, damage=4),Item(cost=10, damage=5),Item(cost=25, damage=6),Item(cost=40, damage=7),Item(cost=74, damage=8)]
armor = [Item(cost=13, armor=1),Item(cost=31, armor=2),Item(cost=53, armor=3),Item(cost=75, armor=4),Item(cost=102, armor=5),Item(cost=0)]
rings = [Item(cost=25, damage=1),Item(cost=50, damage=2),Item(cost=100, damage=3),Item(cost=20, armor=1),Item(cost=40, armor=2),Item(cost=80, armor=3),Item(cost=0),Item(cost=0)]


def is_player_winner(p1: Player) -> bool:
    enemy = Player(armor=2, damage=8)
    turn = "player"
    while p1.hp > 0 and enemy.hp > 0:
        if turn == "player":
            attacker = p1
            defender = enemy
        else:
            attacker = enemy
            defender = p1
        defender.hp -= max(1, attacker.damage - defender.armor)
        turn = "enemy" if turn == "player" else "player"
    if p1.hp <= 0:
        return False
    return True


print("------------PART 1------------")
count = 0
best_cost = math.inf
for weapon_item in weapons:
    for armor_item in armor:
        for ring_items in combinations(rings, 2):
            cost = weapon_item.cost + armor_item.cost + sum(ring.cost for ring in ring_items)
            if cost >= best_cost:
                continue
            armor_val = armor_item.armor + sum(ring.armor for ring in ring_items)
            damage_val = weapon_item.damage + sum(ring.damage for ring in ring_items)
            is_winner = is_player_winner(Player(armor=armor_val, damage=damage_val))
            if is_winner:
                best_cost = cost
            count += 1
print(best_cost)

print("------------PART 2------------")
count = 0
best_cost = -math.inf
for weapon_item in weapons:
    for armor_item in armor:
        for ring_items in combinations(rings, 2):
            cost = weapon_item.cost + armor_item.cost + sum(ring.cost for ring in ring_items)
            if cost <= best_cost:
                continue
            armor_val = armor_item.armor + sum(ring.armor for ring in ring_items)
            damage_val = weapon_item.damage + sum(ring.damage for ring in ring_items)
            is_winner = is_player_winner(Player(armor=armor_val, damage=damage_val))
            if not is_winner:
                best_cost = cost
            count += 1
print(best_cost)