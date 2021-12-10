from collections import defaultdict

prog = []
with open('input23.txt') as f:
    for line in f:
        prog.append(line.strip().split())

mem = defaultdict(int)
def get(val):
    try:
        return int(val)
    except ValueError:
        return mem[val]

cur = 0
z = 0
while cur < len(prog):
    inst, *ops = prog[cur]
    if inst == 'set':
        mem[ops[0]] = get(ops[1])
    elif inst == 'sub':
        mem[ops[0]] = mem[ops[0]] - get(ops[1])
    elif inst == 'mul':
        z += 1
        mem[ops[0]] = mem[ops[0]] * get(ops[1])
    elif inst == 'jnz':
        if get(ops[0]) != 0:
            cur += get(ops[1])
            continue
    else:
        raise ValueError
    cur += 1

print(z)
