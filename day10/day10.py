# AOC
# day 10


filename = 'input.txt'

def part1():
	counter1 = 0
	counter3 = 0

	for i in range(1, len(numbers)):
		if numbers[i] - numbers[i - 1] == 1:
			counter1 += 1
		if numbers[i] - numbers[i - 1] == 3:
			counter3 += 1

	# print('counter1:\t' + str(counter1))
	# print('counter3:\t' + str(counter3))
	print(counter1 * counter3)


def process_group(group):
	if len(group) == 0:
		print('NOOO')
	elif len(group) == 1:
		return 1
	elif len(group) == 2:
		return 1
	else:
		D = 1
		for i in range(1, len(group) - 1):
			if (group[i + 1] - group[i]) == 1:
				D *= 2
		if 8==D:
			D -= 1
		return D


def part2():
	total_combinations = 1
	i = 1
	group = [numbers[0]]

	while i < len(numbers):
		if numbers[i] - numbers[i - 1] < 3:
			group.append(numbers[i])
		else:
			# print(group)
			group_combinations = process_group(group)
			# print(group_combinations)
			# print('\n')
			total_combinations *= group_combinations
			group = [numbers[i]]
		i += 1

	print(total_combinations)		

with open(filename, 'r') as f:
	lines = f.readlines()
	numbers = [int(line.strip()) for line in lines]
	numbers.sort()
	numbers.insert(0, 0)
	numbers.append(numbers[-1] + 3)


part1()
part2()

