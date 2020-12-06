# advent of code
# day 6

with open('input.txt', 'r') as file:
	lines = file.readlines()

	answers = set()
	result = 0

	for line in lines:

		if line == '\n':
			 # print(answers)
			result += len(answers)
			answers.clear()
			# print('===================')
		else:
			line = line.strip()
			for ch in line:
				answers.add(ch)
		

	print(result)

