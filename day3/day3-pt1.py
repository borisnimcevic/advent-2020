# Advent 2020
# day 3 - part 1

with open("input.txt", "r") as file:
    lines = file.readlines()
    index = 0
    counter = 0
    length = len(lines[0]) - 1
    for line in lines:
        if line[index] == '#':
            counter += 1
        index = index + 3
        index = index % length
    print(counter)
