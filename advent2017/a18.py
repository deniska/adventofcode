from collections import defaultdict

prog = []
with open('input18.txt') as f:
    for line in f:
        prog.append(line.strip().split())

mem = defaultdict(int)
def get(val):
    try:
        return int(val)
    except ValueError:
        return mem[val]

cur = 0
freq = 0
while True:
    inst, *ops = prog[cur]
    if inst == 'snd':
        freq = get(ops[0])
    elif inst == 'set':
        mem[ops[0]] = get(ops[1])
    elif inst == 'add':
        mem[ops[0]] = mem[ops[0]] + get(ops[1])
    elif inst == 'mul':
        mem[ops[0]] = mem[ops[0]] * get(ops[1])
    elif inst == 'mod':
        mem[ops[0]] = mem[ops[0]] % get(ops[1])
    elif inst == 'rcv':
        if get(ops[0]):
            print(freq)
            break
    elif inst == 'jgz':
        if get(ops[0]) > 0:
            cur += get(ops[1])
            continue
    else:
        raise ValueError
    cur += 1


