# Used https://stackoverflow.com/questions/33070950/letter-scores-in-python
def get_score_part1():

    score = 0
    scoring_guide = {'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3 + 0,
                     'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
                     'C X': 1 + 6, 'C Y': 2 + 0, 'C Z': 3 + 3}

    # read file
    f = open("Day2Input.txt", "r")

    # iterate through every line, add up sums for each elf and deposit in the calorie list
    while True:
        line = f.readline()
        if not line: break
        score += scoring_guide[line.strip("\n")]

    f.close()
    print(f"Score if XYZ is what you play (Rock, Paper, Scissors): {score}")


def get_score_part2():

    score = 0
    scoring_guide = {'A X': 3 + 0, 'A Y': 1 + 3, 'A Z': 2 + 6,
                     'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
                     'C X': 2 + 0, 'C Y': 3 + 3, 'C Z': 1 + 6}

    # read file
    f = open("Day2Input.txt", "r")

    while True:
        line = f.readline()
        if not line: break
        score += scoring_guide[line.strip("\n")]

    f.close()
    print(f"Score if XYZ is the outcome (Lose, Draw, Win): {score}")


if __name__ == "__main__":
    get_score_part1()
    get_score_part2()