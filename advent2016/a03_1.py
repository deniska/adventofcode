possible = 0

def is_possible(*sides):
    return (sides[0] < sides[1] + sides[2]
            and sides[1] < sides[2] + sides[0]
            and sides[2] < sides[0] + sides[1])

with open('input3.txt') as f:
    for line1, line2, line3 in zip(*[f]*3):
        sides1 = [int(x) for x in line1.split()]
        sides2 = [int(x) for x in line2.split()]
        sides3 = [int(x) for x in line3.split()]
        possible += is_possible(sides1[0], sides2[0], sides3[0])
        possible += is_possible(sides1[1], sides2[1], sides3[1])
        possible += is_possible(sides1[2], sides2[2], sides3[2])
print(possible)
