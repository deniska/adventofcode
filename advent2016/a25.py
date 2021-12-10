import itertools
from itertools import islice

def run(progr, a=0):
    regs = {'a': a, 'b': 0, 'c': 0}
    ptr = 0
    while ptr < len(progr):
        #inst, *ops = progr[ptr]
        inst = progr[ptr][0]
        ops = progr[ptr][1:]
        if inst == 'cpy':
            if ops[0] in regs:
                regs[ops[1]] = regs[ops[0]]
            else:
                regs[ops[1]] = int(ops[0])
        elif inst == 'inc':
            regs[ops[0]] += 1
        elif inst == 'dec':
            regs[ops[0]] -= 1
        elif inst == 'jnz':
            if ops[0] in regs:
                op = regs[ops[0]]
            else:
                op = int(ops[0])
            if op != 0:
                ptr += int(ops[1]) - 1
        elif inst == 'out':
            yield regs[ops[0]]
        ptr += 1

def str_to_prog(s):
    prog = []
    for l in s.splitlines():
        prog.append(l.strip().split())
    return prog

d = 15

if __name__ == '__main__':
    with open('input25.txt') as f:
        s = f.read()

    prog = str_to_prog(s)
    zero_one = list(islice(itertools.cycle([0, 1]), d))

    for i in itertools.count(1):
        if list(islice(run(prog, i), d)) == zero_one:
            print(i)
            break
