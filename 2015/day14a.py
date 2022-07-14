from dataclasses import dataclass


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


@dataclass
class Reindeer:
    name: str
    speed: int
    run_duration: int
    rest_duration: int


def get_deer():
    deer = []
    for line in input.splitlines():
        words = line.split()
        deer.append(Reindeer(words[0], int(words[3]), int(words[6]), int(words[-2])))
    return deer


def get_distance(deer):
    macro_time_step = deer.run_duration + deer.rest_duration
    macro_steps = final_time // macro_time_step
    remainder = min(final_time % macro_time_step, deer.run_duration)
    return ((macro_steps * deer.run_duration) + remainder) * deer.speed


if __name__ == "__main__":
    deer_list = get_deer()
    deer_winner = max(deer_list, key=get_distance)
    print(f"Deer winner: {deer_winner.name}")
    print(f"Deer distance: {get_distance(deer_winner)}")
