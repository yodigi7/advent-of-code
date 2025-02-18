from dataclasses import dataclass
from itertools import combinations
from typing import List
from enum import Enum
from copy import deepcopy
import math


class Spell(Enum):
    MISSILE = 1
    DRAIN = 2
    SHIELD = 3
    POISON = 4
    RECHARGE = 5


SPELL_COSTS = {
    Spell.MISSILE: 53,
    Spell.DRAIN: 73,
    Spell.SHIELD: 113,
    Spell.POISON: 173,
    Spell.RECHARGE: 229,
}


@dataclass
class PoisonEffect:
    duration: int = 6


@dataclass
class ShieldEffect:
    duration: int = 6


@dataclass
class RechargeEffect:
    duration: int = 5


@dataclass
class Player:
    armor: int = 0
    damage: int = 0
    poison: PoisonEffect | None = None
    shield: ShieldEffect | None = None
    recharge: RechargeEffect | None = None
    hp: int = 100
    mana: int = 500

    def tick(self):
        if self.shield:
            self.shield.duration -= 1
            if self.shield.duration <= 0:
                self.shield = None
        if self.poison:
            self.poison.duration -= 1
            self.hp -= 3
            if self.poison.duration <= 0:
                self.poison = None
        if self.recharge:
            self.recharge.duration -= 1
            self.mana += 101
            if self.recharge.duration <= 0:
                self.recharge = None


def is_invalid(p1: Player, enemy: Player, spell: Spell) -> bool:
    if spell == Spell.RECHARGE and p1.recharge and p1.recharge.duration > 1:
        return True
    elif spell == Spell.SHIELD and p1.shield and p1.shield.duration > 1:
        return True
    elif spell == Spell.POISON and enemy.poison and enemy.poison.duration > 1:
        return True

def exec_turn(p1: Player, enemy: Player, spell: Spell, acc: int) -> int:
    '''
    Execute player turn then enemy turn, then return the cost of the spells recursively
    '''
    global best
    global PART2
    if acc >= best or is_invalid(p1, enemy, spell):
        return math.inf
    if p1.hp <= 0:
        return math.inf
    if enemy.hp <= 0:
        # print(f"found winner, spell: {spell}, acc: {acc}")
        best = min(best, acc)
        return acc
    spell_cost = SPELL_COSTS[spell]
    for i in range(2):
        if i == 0 and PART2:
            p1.hp -= 1
            if p1.hp <= 0:
                break
        p1.tick()
        enemy.tick()
        if enemy.hp < 0:
            break

        if i == 0:
            # apply spell
            p1.mana -= spell_cost
            if p1.mana < 0:
                # Invalid
                return math.inf
            match spell:
                case Spell.MISSILE:
                    enemy.hp -= 4
                case Spell.DRAIN:
                    p1.hp += 2
                    enemy.hp -= 2
                case Spell.SHIELD:
                    p1.shield = ShieldEffect()
                case Spell.POISON:
                    enemy.poison = PoisonEffect()
                case Spell.RECHARGE:
                    p1.recharge = RechargeEffect()
        else:
            # Enemy attack
            armor = p1.armor
            if p1.shield:
                armor += 7
            p1.hp -= max(1, enemy.damage - armor)
    return min(exec_turn(deepcopy(p1), deepcopy(enemy), spell, acc + spell_cost) for spell in Spell)




print("------------PART 1------------")
p1 = Player(hp=50)
enemy = Player(hp=51, damage=9)
PART2 = False
best = math.inf
acc = 0
exec_turn(deepcopy(p1), deepcopy(enemy), Spell.POISON, acc)
print(best)
# print(min(exec_turn(deepcopy(p1), deepcopy(enemy), spell, 0) for spell in Spell))

print("------------PART 2------------")
p1 = Player(hp=50)
enemy = Player(hp=50, damage=9)

PART2 = True
acc = 0
best = math.inf
exec_turn(deepcopy(p1), deepcopy(enemy), Spell.POISON, acc)
print(best)