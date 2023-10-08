from functools import partial

class Monkey:
    def __init__(self, number, operation, test):
        self.number = number
        self.operation = operation
        self.test = test
        self.items = []
        self.inspect_count = 0
        self.true_monkey = None
        self.false_monkey = None

    def add_item(self, item_value):
        self.items.append(item_value)

    def inspect_items(self):
        self.inspect_count += len(self.items)
        while self.items:
            item = self.items.pop()
            item = self.operation(item)
            # item = item // 3
            item = item % 9_699_690
            if item % self.test == 0:
                self.true_monkey.add_item(item)
            else:
                self.false_monkey.add_item(item)

    def __lt__(self, other):
        return self.inspect_count < other.inspect_count

def summation(val, inp):
    return val + inp

def mult(val, inp):
    return val*inp

if __name__ == "__main__":
    with open("day11.txt", "r") as f:
        lines = f.readlines()
    monkey_lines = []
    monkey_line = []
    # split up into a list of lines for each monkey
    for line in lines:
        if line == '\n':
            monkey_lines.append(monkey_line)
            monkey_line = []
        else:
            monkey_line.append(line.strip())
    monkey_lines.append(monkey_line)
    monkeys_dict = {}
    # extract all of the information from the group of lines to create a monkey
    for monkey in monkey_lines:
        number = int(monkey[0][7])
        items = [int(item) for item in monkey[1][16:].split(', ')]
        operation = monkey[2][21]
        operation_value = monkey[2][23:]
        test = int(monkey[3][19:])
        true_monkey = int(monkey[4].removeprefix('If true: throw to monkey '))
        false_monkey = int(monkey[5].removeprefix('If false: throw to monkey '))
        if operation == '+':
            op = partial(summation, int(operation_value))
        else:
            if operation_value == 'old':
                op = lambda x: x*x
            else:
                op = partial(mult, int(operation_value))
        monkey = Monkey(number, op, test)
        monkey.items = items
        monkey.true_monkey = true_monkey
        monkey.false_monkey = false_monkey
        monkeys_dict[number] = monkey
    monkeys = list(monkeys_dict.values())
    # go back and connect all of the monkeys
    for monkey in monkeys:
        monkey.true_monkey = monkeys_dict[monkey.true_monkey]
        monkey.false_monkey = monkeys_dict[monkey.false_monkey]

    # for _ in range(20):
    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspect_items()

    monkeys = sorted(monkeys, reverse=True)
    inspect_counts = sorted([monkey.inspect_count for monkey in monkeys_dict.values()])
    print(inspect_counts[-1] * inspect_counts[-2])
