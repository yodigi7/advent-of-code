if __name__ == "__main__":
    priority_sum = 0
    with open('day03.txt', 'r') as inputfile:
        for line in inputfile.readlines():
            sack = line.rstrip()
            first = set(sack[:len(sack)//2])
            second = set(sack[len(sack)//2:])
            common_item = next(iter(first & second))
            if common_item.islower():
                priority_sum += ord(common_item) - 96
            else:
                priority_sum += ord(common_item) - 38
    print(priority_sum)
