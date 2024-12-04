if __name__ == "__main__":
    with open('day01.txt', 'r') as inputfile:
        diff_sum = 0
        list1 = []
        list2 = []
        for line in inputfile.readlines():
            items = line.split("   ")
            item1, item2 = int(items[0]), int(items[1])
            list1.append(int(items[0]))
            list2.append(int(items[1]))
        list1.sort()
        list2.sort()
        for i in range(len(list1)):
            diff_sum += abs(list1[i] - list2[i])
    print(f"Sum of differences: {diff_sum}")
