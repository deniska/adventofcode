
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
            if ops[1] in regs:
                op2 = regs[ops[1]]
            else:
                op2 = int(ops[1])
            if op != 0:
                ptr += op2 - 1
        elif inst == 'tgl':
            if ops[0] in regs:
                op = regs[ops[0]]
            else:
                op = int(ops[0])
            if ptr + op < len(progr):
                p = progr[ptr+op]
                if len(p) == 2:
                    if p[0] == 'inc':
                        p[0] = 'dec'
                    else:
                        p[0] = 'inc'
                else:
                    if p[0] == 'jnz':
                        p[0] = 'cpy'
                    else:
                        p[0] = 'jnz'

        ptr += 1
    print(regs['a'])

def str_to_prog(s):
    prog = []
    for l in s.splitlines():
        prog.append(l.strip().split())
    return prog

s = '''cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 83 c
jnz 78 d
inc a
inc d
jnz d -2
inc c
jnz c -5'''
prog = str_to_prog(s)

run(str_to_prog(s), 7)
run(str_to_prog(s), 12)

