# Advent 2020
# day 3 - part 2


with open("input.txt", "r") as file:
    lines = file.readlines()
    right = [1, 3, 5, 7, 1]
    indices = [0] * 5  # 1, 3, 5, 7, 1&2
    counters = [0] * 5
    length = len(lines[0]) - 1
    for line_index in range(len(lines)):
        for i in range(4):
            if lines[line_index][indices[i]] == '#':
                counters[i] += 1
            indices[i] = indices[i] + right[i]
            indices[i] = indices[i] % length

        if line_index % 2 == 0:
            if lines[line_index][indices[4]] == '#':
                counters[4] += 1
            indices[4] = indices[4] + right[4]
            indices[4] = indices[4] % length

    product = 1
    for counter in counters:
        product = product * counter
    print(product)
