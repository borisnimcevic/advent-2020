# advent of code
# day 8 part 1

filename = 'input.txt'



def execute_instructions():
	accumulator = 0

	with open(filename, 'r') as file:
		lines = file.readlines()
		lines_seen = set()

		i = 0
		while i < len(lines):
			if i in lines_seen:
				return accumulator

			lines_seen.add(i)
			parts = lines[i].split(' ')
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


print(execute_instructions())