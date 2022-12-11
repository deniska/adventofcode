import sys

reg = 1
states = []


with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if line == 'noop':
            states.append(reg)
        else:
            val = int(line.split()[1])
            states.append(reg)
            states.append(reg)
            reg += val

strengths = (20*states[19] + 60*states[59] + 100*states[99]
        + 140*states[139] + 180*states[179] + 220*states[219])
print(strengths)

for cycle, state in enumerate(states, start=1):
    x = cycle % 40 - 1
    if abs(x - state) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if cycle % 40 == 0 and cycle > 0:
        print()
print()
