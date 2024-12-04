from collections import Counter
if __name__ == "__main__":
    with open('day01.txt', 'r') as inputfile:
        similarity = 0
        list1 = []
        list2 = []
        for line in inputfile.readlines():
            items = line.split("   ")
            item1, item2 = int(items[0]), int(items[1])
            list1.append(int(items[0]))
            list2.append(int(items[1]))
        list1.sort()
        list2_count = Counter(list2)
        for i in list1:
            similarity += i * list2_count[i]
    print(f"Similarity: {similarity}")