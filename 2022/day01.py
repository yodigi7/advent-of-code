if __name__ == "__main__":
    with open('day01.txt', 'r') as inputfile:
        maximum_calories = -1
        elves_calories = []
        elf_calories = 0
        for line in inputfile.readlines():
            try:
                calories = int(line)
                elf_calories += calories
            except ValueError:
                elves_calories.append(elf_calories)
                elf_calories = 0
        sorted_list = sorted(elves_calories, reverse=True)[:3]
        print(sorted_list)
        print(sum(sorted_list))
