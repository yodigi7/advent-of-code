import hashlib
from itertools import count

input = "yzbqklnj"


def get_hash(num):
    return hashlib.md5(f"{input}{num}".encode()).hexdigest()


def is_valid(num):
    return num[:6] == "000000"


if __name__ == "__main__":
    for count in count(start=100000):
        hash = get_hash(count)
        if is_valid(hash):
            print(f"Winner: {count}")
            break
