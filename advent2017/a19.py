with open('input19.txt') as f:
    world = f.readlines()

row = 0
col = world[0].index('|')
d = 'd'

res = ''
steps = 0
while True:
    steps += 1
    if d == 'd':
        row += 1
    elif d == 'u':
        row -= 1
    elif d == 'l':
        col -= 1
    elif d == 'r':
        col += 1

    n = world[row][col]
    if n in '|-':
        continue
    elif n == '+':
        if d in 'du':
            if world[row][col+1] == '-':
                d = 'r'
            else:
                d = 'l'
        else:
            if world[row+1][col] == '|':
                d = 'd'
            else:
                d = 'u'
    elif n == ' ':
        break
    else:
        res += n

print(res)
print(steps)
