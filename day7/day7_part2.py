# Advent of Code - Day 7 part 2

filename = 'input.txt'

bag_rules = dict()
seen_flag = set()
result = 0


def extract_bags(s):
    s = s.strip()
    parts = s.split(' ')
    number = int(parts[0])
    bag = parts[1] + ' ' + parts[2]
    return (number, bag)


def oneline_search(count, key):
    if len(bag_rules[key]) == 0:
        return 1
    else:
        sum = 0
        for right_side in bag_rules[key]:
            sum += right_side[0] * oneline_search(right_side[0], right_side[1])
        return sum + 1

with open(filename, "r") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.split('contain')
        parent = parts[0][:-6]
        children = parts[1].split(',')
        if len(children) == 1:
            if 'no other bags' in children[0]:
                bag_rules[parent] = []
            else:
                bag_rules[parent] = [extract_bags(children[0])]
        else:
            bags = []
            for child in children:
                bags.append(extract_bags(child))
            bag_rules[parent] = bags
    # print(bag_rules)


print(oneline_search(0, 'shiny gold')-1)

