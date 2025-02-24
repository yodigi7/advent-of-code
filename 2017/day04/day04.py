with open("day04/day04.txt") as f:
    lines = f.readlines()

print("----------PART 1----------")
def all_unique_words(phrase: str) -> bool:
    l = phrase.strip().split(" ")
    s = set(l)
    return len(l) == len(s)

answer = sum(1 for line in lines if all_unique_words(line))
print(answer)

print("----------PART 2----------")
def no_anagrams(phrase: str) -> bool:
    words = phrase.strip().split(" ")
    sets = set()
    for word in words:
        tup = tuple(sorted(word))

        if tup in sets:
            return False
        sets.add(tup)
    return True

answer = sum(1 for line in lines if all_unique_words(line) and no_anagrams(line))
print(answer)