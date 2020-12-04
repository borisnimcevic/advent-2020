# advent of code 
# day 4

filename = 'input.txt'

expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_entry_count = 0
expected_field_count = 0

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line == '\n':
            expected_field_count = 0
        else:
            parts = line.split(' ')
            for part in parts:
                field, value = part.split(':')
                if field in expected_fields:
                    expected_field_count += 1
            if expected_field_count == len(expected_fields):
                expected_field_count = 0
                valid_entry_count += 1

print("final " + str(valid_entry_count))
