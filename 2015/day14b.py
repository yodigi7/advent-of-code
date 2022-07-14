from dataclasses import dataclass


# input = """Vixen can fly 2 km/s for 1 seconds, but then must rest for 2 seconds.
# """
# input = """Vixen can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Rudolph can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
# """
input = """Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.
"""


final_time = 2503
# final_time = 1000


@dataclass
class Reindeer:
    name: str
    speed: int
    run_duration: int
    rest_duration: int
    resting: bool = False
    current_run_rest_time: int = 0
    current_distance: int = 0
    points: int = 0


def get_deer():
    deer = []
    for line in input.splitlines():
        words = line.split()
        deer.append(Reindeer(words[0], int(words[3]), int(words[6]), int(words[-2])))
    return deer


def step(deer_list: list[Reindeer]):
    for deer in deer_list:
        deer.current_run_rest_time += 1
        if deer.resting:
            if deer.current_run_rest_time == deer.rest_duration:
                deer.resting = False
                deer.current_run_rest_time = 0
        elif deer.current_run_rest_time == deer.run_duration:
            deer.resting = True
            deer.current_distance += deer.speed
            deer.current_run_rest_time = 0
        else:
            deer.current_distance += deer.speed
    best_distance = max(deer.current_distance for deer in deer_list)
    for deer in deer_list:
        if deer.current_distance == best_distance:
            deer.points += 1


if __name__ == "__main__":
    deer_list = get_deer()
    for _ in range(final_time):
        step(deer_list)
    winning_deer = max(deer_list, key=lambda deer: deer.points)
    distance_deer = max(deer_list, key=lambda deer: deer.current_distance)
    print(f"Distance deer: {distance_deer.name}")
    print(f"Max distance: {distance_deer.current_distance}")
    print(f"Deer winner: {winning_deer.name}")
    print(f"Deer distance: {winning_deer.current_distance}")
    print(f"Deer points: {winning_deer.points}")
