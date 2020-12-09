# Day 9 Advent of Code 2020

file_name = "input.txt"
preamble = 25

def summation(numbers, target):
    # print(numbers)
    # print(target)
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if int(numbers[i]) + int(numbers[j]) == target:
                # print("Ture " + numbers[i].strip() + " " + numbers[j].strip() + " " + str(target))
                return True
    return False

with open(file_name,'r') as file:
    lines = file.readlines()
    for index in range(len(lines)-preamble-1):
        if not summation(lines[index:index+preamble], int(lines[index+preamble])):
            print(lines[index+preamble])
