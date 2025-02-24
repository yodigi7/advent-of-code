import re
import math
from dataclasses import dataclass

acc_reg = r"a=<(-?\d+),(-?\d+),(-?\d+)>"
vel_reg = r"v=<(-?\d+),(-?\d+),(-?\d+)>"
pos_reg = r"p=<(-?\d+),(-?\d+),(-?\d+)>"

with open("day20/day20.txt") as f:
    accelerations = [tuple(int(x) for x in re.findall(acc_reg, line)[0]) for line in f.readlines()]
with open("day20/day20.txt") as f:
    velocities = [tuple(int(x) for x in re.findall(vel_reg, line)[0]) for line in f.readlines()]
with open("day20/day20.txt") as f:
    positions = [tuple(int(x) for x in re.findall(pos_reg, line)[0]) for line in f.readlines()]

print("----------PART 1----------")
def net_num(tup: tuple[int]) -> int:
    return tup[0] ** 2 + tup[1] ** 2 + tup[2] ** 2

min_val = math.inf
# find lowest acceleration
lowest_acc = []
for i, item in enumerate(accelerations):
    net_acc = net_num(item)
    if net_acc < min_val:
        lowest_acc = [i]
        min_val = net_acc
    elif net_acc == min_val:
        lowest_acc.append(i)
print(lowest_acc)
min_val = math.inf
lowest_vel = []
for i in lowest_acc:
    item = velocities[i]
    net_acc = net_num(item)
    if net_acc < min_val:
        lowest_vel = [i]
        min_val = net_acc
    elif net_acc == min_val:
        lowest_vel.append(i)
print(lowest_vel)

print("----------PART 2----------")

@dataclass
class Particle:
    position: tuple[int]
    velocity: tuple[int]
    acceleration: tuple[int]

    def move(self):
        self.velocity = tuple(sum(x) for x in zip(self.acceleration, self.velocity))
        self.position = tuple(sum(x) for x in zip(self.velocity, self.position))

particles: list[Particle] = []

for i in range(len(accelerations)):
    particles.append(Particle(positions[i], velocities[i], accelerations[i]))

for i in range(1_000):
    part_pos: dict[tuple[int], Particle] = dict()
    used_pos: tuple[int] = set()
    destroy_pos: tuple[int] = set()

    for particle in particles:
        particle.move()
        if particle.position in used_pos:
            destroy_pos.add(particle.position)
        else:
            used_pos.add(particle.position)
            part_pos[particle.position] = particle

    if len(destroy_pos) != 0:
        print(f"Destroying {len(destroy_pos)} particles in step {i}")

    particles = [particle for particle in part_pos.values() if particle.position not in destroy_pos]

print(len(particles))