# advent of code
# day 6

with open('input.txt', 'r') as file:
	lines = file.readlines()

	answers = dict()
	result_part1 = 0
	result_part2 = 0
	num_people = 0
	overlap_answers = 0

	for line in lines:

		if line == '\n':
			# print(answers)
			for answer, count in answers.items():
				if count == num_people:
					overlap_answers += 1

			result_part1 += len(answers)
			result_part2 += overlap_answers
			answers.clear()
			num_people = 0
			overlap_answers = 0
			# print('===================')
		else:
			line = line.strip()
			num_people += 1
			for ch in line:
				if ch in answers.keys():
					answers[ch] += 1
				else:
					answers[ch] = 1
		

	print('Part 1: ' + str(result_part1))
	print('Part 2: ' + str(result_part2))

