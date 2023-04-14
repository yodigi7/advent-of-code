if __name__ == "__main__":
    myscore = 0
    with open('day02.txt', 'r') as inputfile:
        for line in inputfile.readlines():
            opponent, me = line.split()
            game_score = 0
            if (opponent == 'A' and me == 'X') or (opponent == 'B' and me == 'Y') or (opponent == 'C' and me == 'Z'):
                game_score += 3
            elif (opponent == 'A' and me == 'Y') or (opponent == 'B' and me == 'Z') or (opponent == 'C' and me == 'X'):
                game_score += 6
            if me == 'X':
                game_score += 1
            elif me == 'Y':
                game_score += 2
            elif me == 'Z':
                game_score += 3
            myscore += game_score
    print(myscore)
