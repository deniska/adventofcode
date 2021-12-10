import sys

argcount = {1: 3, # add
        2: 3, # mul
        3: 1, # in
        4: 1, # out
        99: 0, # hlt

        5: 2, # jnz
        6: 2, # jz
        7: 3, # lt
        8: 3, # eq
        }

def run(prog, inp=1):
    prog = prog.copy()
    pc = 0
    def arg(n):
        if immediate[n] == 1:
            return prog[pc + n + 1]
        return prog[prog[pc + n + 1]]
    while True:
        opcode = prog[pc]
        immediate = []
        inst = opcode % 100
        for i in range(argcount[inst]):
            if (opcode // 100) // (10 ** i) % 10 == 1:
                immediate.append(True)
            else:
                immediate.append(False)
        if inst == 99:
            break
        elif inst == 1:
            prog[prog[pc + 3]] = arg(0) + arg(1)
        elif inst == 2:
            prog[prog[pc + 3]] = arg(0) * arg(1)
        elif inst == 3:
            prog[prog[pc + 1]] = inp
        elif inst == 4:
            print(arg(0))
        elif inst == 5:
            if arg(0) != 0:
                pc = arg(1)
                continue
        elif inst == 6:
            if arg(0) == 0:
                pc = arg(1)
                continue
        elif inst == 7:
            if arg(0) < arg(1):
                prog[prog[pc + 3]] = 1
            else:
                prog[prog[pc + 3]] = 0
        elif inst == 8:
            if arg(0) == arg(1):
                prog[prog[pc + 3]] = 1
            else:
                prog[prog[pc + 3]] = 0
        pc += argcount[inst] + 1

test_prog = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
run(test_prog, 5)
run(test_prog, 8)
run(test_prog, 10)

def main():
    with open(sys.argv[1]) as f:
        prog = f.read()
    prog = prog.strip().split(',')
    prog = [int(a) for a in prog]
    run(prog, 1)
    run(prog, 5)

if __name__ == '__main__':
    main()
