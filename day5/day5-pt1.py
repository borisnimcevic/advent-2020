# day 5 Advent of code

with open("input.txt", "r") as file:
    lines = file.readlines()
    max_ID = 0
    for line in lines:
        seat_ID = 0
        line = line.strip()
        for char in line:
            if char == 'B' or char == 'R':
                seat_ID = (seat_ID << 1) | 1
            else:
                seat_ID = (seat_ID << 1)
        #print(seat_ID)
        if (seat_ID > max_ID):
            max_ID = seat_ID

print(max_ID)
