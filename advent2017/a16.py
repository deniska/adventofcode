with open('input16.txt') as f:
    s = f.read()

init = 'abcdefghijklmnop'
progs = list(init)

moves = s.split(',')
def dance(progs):
    progs = list(progs)
    for move in moves:
        if move[0] == 's':
            count = int(move[1:])
            progs = progs[-count:] + progs[:-count]
        elif move[0] == 'x':
            pos1, pos2 = [int(a) for a in move[1:].split('/')]
            progs[pos1], progs[pos2] = progs[pos2], progs[pos1]
        else:
            p1, p2 = move[1:].split('/')
            i1 = progs.index(p1)
            i2 = progs.index(p2)
            progs[i1] = p2
            progs[i2] = p1
    return ''.join(progs)

print(dance(progs))

results = [progs]
dances = 1
while True:
    progs = dance(progs)
    if progs == init:
        break
    dances += 1
    results.append(progs)

print(results[1_000_000_000 % dances])
