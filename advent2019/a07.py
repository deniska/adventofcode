from itertools import permutations
from intcode import run
import sys

def main():
    with open(sys.argv[1]) as f:
        prog = f.read().strip().split(',')
    prog = [int(p) for p in prog]
    max_p = 0
    max_phases = None
    for phases in permutations(range(5)):
        p = 0
        for phase in phases:
            inp = [p, phase]
            p = run(prog, inp).pop()
        if p > max_p:
            max_p = p
            max_phases = phases
    print(max_phases)
    print(max_p)

if __name__ == '__main__':
    main()
