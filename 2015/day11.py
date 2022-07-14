input = "cqjxjnds"


def valid_password(string):
    req1 = any(
        True
        for chr1, chr2, chr3 in zip(string[:-2], string[1:-1], string[2:])
        if ord(chr1) == ord(chr2) - 1 == ord(chr3) - 2
    )
    req2 = all(False for chr in string if chr in "iol")
    req3 = (
        len(set(chr1 for chr1, chr2 in zip(string[1:], string[:-1]) if chr1 == chr2))
        > 1
    )
    return req1 and req2 and req3


def increment_password(string):
    if string[-1] == "z":
        return f"{increment_password(string[:-1])}a"
    else:
        return f"{string[:-1]}{chr(ord(string[-1])+1)}"


if __name__ == "__main__":
    input = increment_password(input)
    while not valid_password(input):
        input = increment_password(input)
    print(f"Next valid password: {input}")
