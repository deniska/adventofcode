import sys

t = str.maketrans({'L': '0', 'R': '1', 'F': '0', 'B': '1'})

max_seat = -1
seats = set()
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        seat = int(line.translate(t), 2)
        if seat > max_seat:
            max_seat = seat
        seats.add(seat)

print(max_seat)

seats = sorted(seats)
prev = seats[0]
for seat in seats[1:]:
    if seat - prev == 2:
        print(seat - 1)
        break
    prev = seat

