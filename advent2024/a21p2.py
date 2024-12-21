import sys
import math
import random
import collections
import itertools

codes = []
with open(sys.argv[1]) as f:
    for line in f:
        codes.append(line.strip())

coords_numpad = {
    '7': (0, 0), '8': (1, 0), '9': (2, 0),
    '4': (0, 1), '5': (1, 1), '6': (2, 1),
    '1': (0, 2), '2': (1, 2), '3': (2, 2),
                 '0': (1, 3), 'A': (2, 3),
}

coords_keypad = {
                 '^': (1, 0), 'A': (2, 0),
    '<': (0, 1), 'v': (1, 1), '>': (2, 1),
}

def lr(dx):
    if dx >= 0:
        return '>' * dx
    else:
        return '<' * (-dx)

def ud(dy):
    if dy >= 0:
        return 'v' * dy
    else:
        return '^' * (-dy)

def keypad_dist(a, b):
    ax, ay = coords_keypad[a]
    bx, by = coords_keypad[b]
    return abs(ax - bx) + abs(ay - by)

def iternumpad(code):
    results = [[]]
    prev = 'A'
    for c in code:
        px, py = coords_numpad[prev]
        cx, cy = coords_numpad[c]
        dx = cx - px
        dy = cy - py
        hor = lr(dx)
        ver = ud(dy)
        if prev in '0A' and c in '147':
            # must go up first
            for r in results:
                r.extend(ver)
                r.extend(hor)
        elif c in '0A' and prev in '147':
            # must go down last
            for r in results:
                r.extend(hor)
                r.extend(ver)
        else:
            if dx != 0 and dy != 0:
                new = [r.copy() for r in results]
                for r in new:
                    r.extend(ver)
                    r.extend(hor)
            for r in results:
                r.extend(hor)
                r.extend(ver)
            if dx != 0 and dy != 0:
                results.extend(new)
        for r in results:
            r.append('A')
        prev = c
    return results

def keypad(code):
    prev = 'A'
    prev_keypad = 'A'
    for c in code:
        r = []
        px, py = coords_keypad[prev]
        cx, cy = coords_keypad[c]
        dx = cx - px
        dy = cy - py
        hor = lr(dx)
        ver = ud(dy)
        if c == '<':
            # must go vertically first
            yield ver + hor + 'A'
        elif prev == '<':
            # must go horizontally first
            yield hor + ver + 'A'
        elif dx == 0:
            yield ver + 'A'
        elif dy == 0:
            yield hor + 'A'
        else:
            yield hor + ver + 'A'
            #yield ver + hor + 'A'
        prev = c

#codes = ['805A']
def clen(counter):
    return sum(len(k) * v for (k, v) in counter.items())

def go(n):
    s = 0
    for code in codes:
        minlen = math.inf
        for c in iternumpad(code):
            counter = collections.Counter({''.join(c): 1})
            for i in range(n):
                next_counter = collections.Counter()
                for thing, cnt in counter.items():
                    for part in keypad(thing):
                        next_counter[part] += cnt
                counter = next_counter
                print(counter)
            minlen = min(minlen, clen(counter))
        #print(minlen)
        s += int(code.strip('A')) * minlen
        #print()
    print(s)

# A = prev_a + prev_v*2 + prev_h*2
#go(2)
go(25)
# 474989773944940 too high
# 294667840961390 too high
