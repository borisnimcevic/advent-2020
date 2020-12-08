# advent of code
# day 8 part 2

filename = 'input.txt'


def execute_instructions(index, new_line):
	with open(filename, 'r') as file:
		new_lines = file.readlines()

	new_lines[index] = new_line

	accumulator = 0
	lines_seen = set()

	i = 0
	while i < len(new_lines):
		if i in lines_seen:
			return 0

		lines_seen.add(i)
		parts = new_lines[i].split(' ')
		operation = parts[0]
		argument = int(parts[1])

		if operation == 'acc':
			accumulator += argument
			i += 1
		elif operation == 'jmp':
			i += argument
		elif operation == 'nop':
			i += 1
		else:
			pass

	return accumulator


with open(filename, 'r') as file:
	lines = file.readlines()
	
	for i in range(len(lines)):
		result = 0
		if lines[i][:3] == 'nop':
			result = execute_instructions(i, lines[i].replace('nop', 'jmp')) 
		elif lines[i][:3] == 'jmp':
			result = execute_instructions(i, lines[i].replace('jmp', 'nop')) 
		if result != 0:
			print(result)