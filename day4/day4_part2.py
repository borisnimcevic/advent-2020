# advent of code 
# day 4

filename = 'input.txt'

expected_fields = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid_entry_count = 0
expected_field_count = 0

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line == '\n':
            print("-------")
            expected_field_count = 0
        else:
            line = line.strip()
            parts = line.split(' ')
            for part in parts:
                field, value = part.split(':')
                if field == 'byr':
                    if  1920 <= int(value) <= 2002:
                        print("byr")
                        expected_field_count += 1
                if field == 'iyr':
                    if  2010 <= int(value) <= 2020:
                        print("iyr")
                        expected_field_count += 1
                if field == 'eyr':
                    if  2020 <= int(value) <= 2030:
                        print("eyr")
                        expected_field_count += 1
                if field == 'hgt':
                    if value[-2:] == "cm":
                        if  150 <= int(value[:-2]) <= 193:
                            expected_field_count += 1
                            print("hgt-cm")
                    if value[-2:] == "in":
                        if  59 <= int(value[:-2]) <= 76:
                            expected_field_count += 1
                            print("hgt-in")
                if field == 'hcl':
                    if (value[0] == "#") and (len(value) == 7):
                        char_good = True
                        for char in value[1:]:
                            if not ((ord('0') <= ord(char) <= ord('9')) or (ord('a') <= ord(char) <= ord('f'))):
                                char_good = False
                        if(char_good):
                            expected_field_count += 1
                            print("hcl")

                if field == 'ecl':
                    if value in expected_fields:
                        expected_field_count += 1
                        print("ecl")

                if field == 'pid':
                    if len(value) == 9:
                        char_good = True
                        for char in value:
                            if not char.isnumeric():
                                char_good = False
                        if(char_good):
                            expected_field_count += 1
                            print("pid")
                print(expected_field_count)

            if expected_field_count == 7:
                expected_field_count = 0
                valid_entry_count += 1
                print("good")

print("final " + str(valid_entry_count))
