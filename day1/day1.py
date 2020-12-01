numbers = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        numbers.append(int(line))

def day1():
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result = numbers[i] + numbers[j]
            if result == 2020:
                solution = numbers[i] * numbers[j]
                print("number1 = " + str(numbers[i]))
                print("number2 = " + str(numbers[j]))
                print(solution)
                return

day1()
