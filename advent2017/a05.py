prog = []
with open('input05.txt') as f:
    for line in f:
        prog.append(int(line.strip()))

def run(prog):
    cur = 0
    steps = 0
    prog = list(prog)
    while cur < len(prog):
        inst = prog[cur]
        if inst >= 3:
            prog[cur] -= 1
        else:
            prog[cur] += 1
        steps +=1
        cur += inst
    return steps

print(run(prog))
