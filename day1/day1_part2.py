numbers = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        numbers.append(int(line))

def day1():
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
                for k in range(j + 1, len(numbers)):
                    result = numbers[i] + numbers[j] + numbers[k]
                    if result == 2020:
                        solution = numbers[i] * numbers[j] * numbers[k]
                        print("number1 = " + str(numbers[i]))
                        print("number2 = " + str(numbers[j]))
                        print("number3 = " + str(numbers[k]))
                        print(solution)
                        return

day1()
