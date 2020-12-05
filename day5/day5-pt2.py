# day 5 Advent of code

list_of_IDs = []
max_ID = 0

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        seat_ID = 0
        line = line.strip()
        for char in line:
            if char == 'B' or char == 'R':
                seat_ID = (seat_ID << 1) | 1
            else:
                seat_ID = (seat_ID << 1)
        #print(seat_ID)
        list_of_IDs.append(seat_ID)
        if (seat_ID > max_ID):
            max_ID = seat_ID

print("max = " + str(max_ID))
for index in range(75,max_ID):
    if not (index in list_of_IDs):
        if (index+1 in list_of_IDs) and (index-1 in list_of_IDs):
            print(index)

