# advent coding
# day 2


def check_password_policy(s):
	policy, password = s.split(':')
	letter = policy[-1]
	low, high = policy[:-2].split('-')
	low = int(low)
	high = int(high)
	return low <= password.strip().count(letter) <= high


with open('input.txt', 'r') as file:
	lines = file.readlines()
	s = 0
	for line in lines:
		if check_password_policy(line):
			s += 1
	print(s)

