import sys

draws = {'AX', 'BY', 'CZ'}
wins = {'AY', 'BZ', 'CX'}
loses = {'AZ', 'BX', 'CY'}
vals = {'X': 1, 'Y': 2, 'Z': 3}

inst = []

with open(sys.argv[1]) as f:
    for line in f:
        a, b = line.strip().split()
        inst.append((a, b))

s = 0
for a, b in inst:
    c = a+b
    if c in wins:
        s += 6
    elif c in draws:
        s += 3
    else:
        s += 0
    s += vals[b]
print(s)


to_lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
to_draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
s = 0
for a, b in inst:
    if b == 'X':
        s += 0
        s += vals[to_lose[a]]
    elif b == 'Y':
        s += 3
        s += vals[to_draw[a]]
    elif b == 'Z':
        s += 6
        s += vals[to_win[a]]
print(s)
