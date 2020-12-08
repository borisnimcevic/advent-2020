# Advent of Code - Day 7

bag_rules = dict()
seen_flag = set()
result = 0

def extract_bags(s):
    s = s.strip()
    parts = s.split(' ')
    #number = int(parts[0])
    bag = parts[1] + ' ' + parts[2]
    #return (number,bag)
    return bag

def find_bag(bag_type, counter):
    counter+=1
    # print(bag_type)
    if bag_type in seen_flag:
        counter-=1
    else:
        seen_flag.add(bag_type)
    if len(bag_rules[bag_type]) == 0:
        # print("Last bag")
        return 0
    else:
        sum = 0
        for righ_side in bag_rules[bag_type]:
            if righ_side == 'shiny gold':
                # print("It's shiny gold! " + str(counter))
                sum = counter
                counter = 0
            else:
                sum += find_bag(righ_side,counter)
                counter = 0
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
    result += find_bag(left,0)

# result = find_bag('muted yellow', 0)
print(result)
