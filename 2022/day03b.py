import string
if __name__ == "__main__":
    priority_sum = 0
    with open('day03.txt', 'r') as inputfile:
        readlines = inputfile.readlines()
        lines = map(lambda line: line.rsplit(), readlines)
        groups = zip(lines, lines, lines)
        for group in groups:
            badge_set = set(string.ascii_letters)
            for member in group:
                badge_set = badge_set & set(member[0])
            badge = next(iter(badge_set))
            if badge.islower():
                priority_sum += ord(badge) - 96
            else:
                priority_sum += ord(badge) - 38
    print(priority_sum)
