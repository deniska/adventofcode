import sys
import pathlib

lines = pathlib.Path(sys.argv[1]).read_text().strip().split('\n')
prog = []

for line in lines:
    inst, param = line.split()
    param = int(param)
    prog.append((inst, param))

def run(prog):
    pc = 0
    acc = 0
    visited = set()
    while pc < len(prog):
        if pc in visited:
            return acc, False
        visited.add(pc)
        inst, param = prog[pc]
        if inst == 'acc':
            acc += param
            pc += 1
        elif inst == 'jmp':
            pc += param
        else:
            pc += 1
    return acc, True

print(run(prog)[0])

for i, (inst, param) in enumerate(prog):
    if inst == 'nop':
        inst = 'jmp'
    elif inst == 'jmp':
        inst = 'nop'
    else:
        continue
    prog1 = prog.copy()
    prog1[i] = (inst, param)
    acc, finished = run(prog1)
    if finished:
        print(acc)
        break

