# Day 9 Advent of Code 2020

file_name = "input.txt"
preamble = 25
part1_solution = 0

# Part 1
def summation(numbers, target):
    # print(numbers)
    # print(target)
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if int(numbers[i]) + int(numbers[j]) == target:
                # print("Ture " + numbers[i].strip() + " " + numbers[j].strip() + " " + str(target))
                return True
    return False

# Part 2
def decryption(target):
    for index in range(len(lines)):
        i = 0
        result = 0
        while result < target:
            if (index + i > len(lines)):
                print("Out of scope")
                break
            else:
                result += int(lines[index + i])
                i  += 1
                if result == target:
                    return (index, index+i)
    print("should never get here")
    return 0

# Find the min 

with open(file_name,'r') as file:
    lines = file.readlines()
    for index in range(len(lines)-preamble-1):
        if not summation(lines[index:index+preamble], int(lines[index+preamble])):
            part1_solution  = int(lines[index+preamble])
            print(lines[index+preamble])

left, right = decryption(part1_solution)
int_list = [int(x) for x in lines[left:right]]
print(int(min(int_list)) + int(max(int_list)))
