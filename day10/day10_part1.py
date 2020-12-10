# AOC
# day 10


filename = 'input.txt'

with open(filename, 'r') as f:
	lines = f.readlines()
	numbers = [int(line.strip()) for line in lines]
	numbers.sort()


	counter1 = 0
	counter3 = 1
	if numbers[0] == 1: counter1 += 1
	if numbers[0] == 3: counter3 += 1

	for i in range(1, len(numbers)):
		if numbers[i] - numbers[i - 1] == 1:
			counter1 += 1
		if numbers[i] - numbers[i - 1] == 3:
			counter3 += 1

	print('counter1:\t' + str(counter1))
	print('counter3:\t' + str(counter3))
	print(counter1 * counter3)
