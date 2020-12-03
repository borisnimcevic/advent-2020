# advent coding
# day 2

def check_password_policy(s):
    policy, password = s.split(':')
    letter = policy[-1]
    low, high = policy[:-2].split('-')
    low = int(low)
    high = int(high)
    password = password.strip()
    pas_len = len(password)
    if pas_len < low:
        return False

    A = True if (password[low-1] == letter) else False

    if pas_len < high:
        return A

    B = True if (password[high-1] == letter) else False
    return A^B

with open('input.txt', 'r') as file:
	lines = file.readlines()
	s = 0
	for line in lines:
		if check_password_policy(line):
			s += 1
	print(s)

