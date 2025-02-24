with open("day06/day06.txt") as f:
    banks = tuple(int(x) for x in f.readline().split("\t"))
original_banks = banks

def redistribute(tup: tuple[int]) -> tuple[int]:
    banks = list(tup)
    m = max(banks)
    i = banks.index(m)
    size = len(banks)
    banks[i] = 0
    multiplier = m // size
    extras = m % size
    for j in range(len(banks)):
        banks[j] += multiplier
    for j in range(extras):
        banks[(i+j+1)%size] += 1
    return tuple(banks)


print("----------PART 1----------")
states = set()
cycles = 0
while banks not in states:
    states.add(banks)
    banks = redistribute(banks)
    cycles += 1
print(cycles)


print("----------PART 2----------")
states = []
banks = original_banks
while banks not in states:
    states.append(banks)
    banks = redistribute(banks)
print(cycles - states.index(banks))