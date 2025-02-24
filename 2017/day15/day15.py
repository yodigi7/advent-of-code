divisor = 2147483647
a_start = 65
b_start = 8921
a_start = 699
b_start = 124
def create_gen(start: int, factor: int):
    global divisor
    value = start
    while True:
        yield value
        value = (factor * value) % divisor

gen_a = create_gen(a_start, 16807)
gen_b = create_gen(b_start, 48271)

print("----------PART 1----------")
# count = 0
# for i in range(40_000_000):
#     vala, valb = bin(next(gen_a))[2:][-16:].zfill(16), bin(next(gen_b))[2:][-16:].zfill(16)
#     if vala == valb:
#         count += 1
# print(count)
print(sum(1 for _ in range(40_000_000) if bin(next(gen_a))[2:][-16:].zfill(16) == bin(next(gen_b))[2:][-16:].zfill(16)))
# print(sum(1 for _ in range(40_000_000) if bin(next(gen_a))[-16:] == bin(next(gen_b))[-16:]))

print("----------PART 2----------")

def create_gen(start: int, factor: int, multiple: int):
    global divisor
    value = start
    while True:
        if value % multiple == 0:
            yield value
        value = (factor * value) % divisor

gen_a = create_gen(a_start, 16807, 4)
gen_b = create_gen(b_start, 48271, 8)
print(sum(1 for _ in range(5_000_000) if bin(next(gen_a))[2:][-16:].zfill(16) == bin(next(gen_b))[2:][-16:].zfill(16)))
