possible = 0

with open('input3.txt') as f:
    for line in f:
        sides = [int(x) for x in line.split()]
        possible += (sides[0] < sides[1] + sides[2]
                and sides[1] < sides[2] + sides[0]
                and sides[2] < sides[0] + sides[1])
print(possible)
