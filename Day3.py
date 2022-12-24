# this provides a good summary of execution methods
# https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string

def sum_priorities_part_1():

    priorities_sum = 0

    # read file
    f = open("Day3Input.txt", "r")

    # iterate through every line, add up sums for each elf and deposit in the calorie list
    while True:
        line = f.readline().strip('\n')
        if not line: break

        # break the rucksack into its compartments (half and half)
        first = line[:int((len(line))/2)]
        second = line[-int((len(line))/2):]

        # get the common character between the first and second halves
        common = set(first) & set(second)
        common = common.pop()

        # assuming theres only one common character
        if common.isupper():
            priorities_sum += ord(common) - ord('A') + 27
        else:
            priorities_sum += ord(common) - ord('a') + 1

    f.close()

    print(priorities_sum)


def sum_priorities_part_2():

    priorities_sum = 0

    # read file
    f = open("Day3Input.txt", "r")

    # iterate through every line, add up sums for each elf and deposit in the calorie list
    while True:
        first = f.readline().strip('\n')
        if not first: break
        second = f.readline().strip('\n')
        third = f.readline().strip('\n')

        # get the common character between the first and second halves
        common = set(first) & set(second) & set(third)
        common = common.pop()

        # assuming theres only one common character
        if common.isupper():
            priorities_sum += ord(common) - ord('A') + 27
        else:
            priorities_sum += ord(common) - ord('a') + 1

    f.close()

    print(priorities_sum)


if __name__ == "__main__":
    sum_priorities_part_1()
    sum_priorities_part_2()