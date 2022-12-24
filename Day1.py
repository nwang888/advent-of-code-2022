def find_caloric_elf():
    # read file
    f = open("Day1Input.txt", "r")
    file = f.readlines()
    f.close()

    # save index of elf with max sum, save max sum
    elf_index = 0
    cur_sum = 0
    max_sum = 0
    max_elf_index = 0

    # iterate through each line of the file and sum the rows until we hit a whitespace line
    for line in file:
        if line == '\n':
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_elf_index = elf_index
                elf_index += 1
                cur_sum = 0
        else:
            cur_sum += int(line)

    print(elf_index, max_sum)


def get_calorie_list():
    calorie_list = []

    # read file
    f = open("Day1Input.txt", "r")

    cur_sum = 0

    # iterate through every line, add up sums for each elf and deposit in the calorie list
    while True:
        line = f.readline()
        if not line: break
        if line == '\n':
            calorie_list.append(cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(line)

    f.close()
    calorie_list_sums = sorted(calorie_list, reverse=True)
    print("Calorie Count of Top 3 Elves")
    print(calorie_list_sums[0], calorie_list_sums[1], calorie_list_sums[2])


if __name__ == "__main__":
    get_calorie_list()
