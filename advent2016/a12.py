def run(progr, c=0):
    regs = {'a': 0, 'b': 0, 'c': c}
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
        ptr += 1
    print(regs['a'])

def str_to_prog(s):
    prog = []
    for l in s.splitlines():
        prog.append(l.strip().split())
    return prog

run(str_to_prog('''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''))
s = '''cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 14 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5'''
run(str_to_prog(s))
run(str_to_prog(s), 1)
