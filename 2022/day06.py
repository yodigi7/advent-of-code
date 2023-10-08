if __name__ == "__main__":
    with open('day06.txt', 'r') as inputfile:
        datastream = inputfile.read()
        offset = 0
        WINDOW = 14
        while True:
            marker = datastream[offset:offset+WINDOW]
            if len(set(marker)) == WINDOW or offset >= len(datastream):
                print(offset+WINDOW)
                break
            print(marker)
            offset += 1
