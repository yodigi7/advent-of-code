input = "3113322113"


def look_and_say(num):
    res_num = ""
    prev_char = num[0]
    count = 0
    for char in num:
        if char != prev_char:
            res_num += str(count) + prev_char
            prev_char = char
            count = 0
        count += 1
    res_num += str(count) + char
    return res_num


if __name__ == "__main__":
    for i in range(50):
        input = look_and_say(input)
    print(len(input))
