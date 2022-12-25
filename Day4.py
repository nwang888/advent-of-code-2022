# https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python

def count_contained_pairs():

    count = 0

    # read file
    f = open("Day4Input.txt", "r")

    while True:
        line = f.readline().strip('\n')
        if not line: break

        assignments = line.split(',')

        first = assignments[0].split('-')
        second = assignments[1].split('-')

        lower_diff = int(first[0]) - int(second[0])
        upper_diff = int(first[1]) - int(second[1])

        if (lower_diff >= 0 and upper_diff <= 0) or (lower_diff <= 0 and upper_diff >= 0):
            count += 1

    f.close()

    print(count)


def count_overlapping_pairs():

    count = 0

    # read file
    f = open("Day4Input.txt", "r").readlines()

    for line in f:
        line.strip('\n')

        assignments = line.split(',')

        first = assignments[0].split('-')
        second = assignments[1].split('-')

        # if the end of the second is greater than the start of first or
        # if the end of the first is greater than the start of the second, then they overlap
        if second[1] >= first[0] >= second[0]:
            count += int(second[1]) - int(first[0]) + 1
        elif second[1] >= first[1] >= second[0]:
            count += int(first[1]) - int(second[0]) + 1

    print(count)


def count_overlapping_pairs_2():
    # uses set intersect
    count = 0

    # read file
    f = open("Day4Input.txt", "r").readlines()

    for line in f:
        line.strip('\n')

        assignments = line.split(',')

        first = assignments[0].split('-')
        second = assignments[1].split('-')

        if set(range(int(first[0]), int(first[1]))) & set(range(int(second[0]),int(second[1]))):
            count += 1

    print(count)

def count_overlapping_pairs_3():
    # range intersection
    count = 0

    # read file
    f = open("Day4Input.txt", "r").readlines()

    for line in f:
        line.strip('\n')

        assignments = line.split(',')

        first = assignments[0].split('-')
        second = assignments[1].split('-')

        if range(max(int(first[0]),int(second[0])), min(int(first[1]),int(second[1]))):
            count += 1

    print(count)


def correct_pt2():
    # ngl I still don't understand why this works but the others don't
    f = open("Day4input.txt", "r").read().splitlines()

    count = 0

    for line in f:

        first, second = line.split(",")

        first_start, first_end = [int(r) for r in first.split("-")]
        second_start, second_end = [int(r) for r in second.split("-")]

        if second_end >= first_start >= second_start or first_end >= second_start >= first_start:
            count += 1

    print(count)


if __name__ == "__main__":
    count_contained_pairs()
    count_overlapping_pairs_3()
    correct_pt2()