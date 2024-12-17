import itertools
import sys

with open(sys.argv[1]) as f:
    A = int(f.readline().strip().partition(': ')[2])
    B = int(f.readline().strip().partition(': ')[2])
    C = int(f.readline().strip().partition(': ')[2])
    f.readline()
    prog = [int(x) for x in f.readline().strip().partition(': ')[2].split(',')]

def combo(A, B, C, operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    raise ValueError(f'Invalid combo operand {operand}')

def run(A, B, C, prog):
    out = []
    i = 0
    while i < len(prog):
        opcode = prog[i]
        operand = prog[i+1]
        i += 2
        if opcode == 0:
            A = A // (2**combo(A, B, C, operand))
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = combo(A, B, C, operand) & 0b111
        elif opcode == 3:
            if A != 0:
                i = operand
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            out.append(combo(A, B, C, operand) & 0b111)
        elif opcode == 6:
            B = A // (2**combo(A, B, C, operand))
        elif opcode == 7:
            C = A // (2**combo(A, B, C, operand))
    return out

print(','.join(str(c) for c in run(A, B, C, prog)))

step = 1
A = 0
while True:
    res = run(A, B, C, prog)
    #if len(res) > len(prog):
    #    print(oct(step), oct(A), res, prog)
    #    print('fail')
    #    break
    if res == prog[:len(res)] and A != 0o622353727236017:
        step = 2 ** A.bit_length()
        #print(oct(step), oct(A), res, prog)
    if res == prog:
        break
    A += step

print(A)
