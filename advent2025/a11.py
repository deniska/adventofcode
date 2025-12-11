import sys
import functools

cons = {}

with open(sys.argv[1]) as f:
    for line in f:
        inp, _, out = line.partition(': ')
        out = out.split()
        cons[inp] = out

@functools.cache
def find(start, finish):
    s = 0
    for c in cons.get(start, []):
        if c == finish:
            s += 1
        else:
            s += find(c, finish)
    return s

p1 = find('you', 'out')
print(p1)

p2 = find('svr', 'fft') * find('fft', 'dac') * find('dac', 'out')
print(p2)
