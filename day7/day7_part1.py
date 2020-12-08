# Advent of Code - Day 7

bag_rules = dict()
seen_flag = set()
result = 0
global_counter = 0

def extract_bags(s):
    s = s.strip()
    parts = s.split(' ')
    #number = int(parts[0])
    bag = parts[1] + ' ' + parts[2]
    #return (number,bag)
    return bag


def oneline_search(key):
    if len(bag_rules[key]) == 0:
        return 0
    else:
        sum = 0
        for right_side in bag_rules[key]:
            if right_side == 'shiny gold':
                return 1
            else:
                sum += oneline_search(right_side)
        return sum

with open("input.txt", "r") as file:
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
    print(bag_rules)

for left in bag_rules.keys():
    if oneline_search(left):
        global_counter +=1 

print(global_counter)
