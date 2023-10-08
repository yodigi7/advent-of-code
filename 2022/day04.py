if __name__ == "__main__":
    count = 0
    with open('day04.txt', 'r') as inputfile:
        for line in inputfile.readlines():
            range1, range2 = line.split(",")
            range1 = tuple(map(int, range1.split("-")))
            range2 = tuple(map(int, range2.split("-")))
            if (range1[0] >= range2[0] and range1[1] <= range2[1]) or (range1[0] <= range2[0] and range1[1] >= range2[1]):
                count += 1
    print(count)
