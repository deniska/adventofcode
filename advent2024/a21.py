import sys

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

def iterkeypad(code):
    results = [[]]
    prev = 'A'
    for c in code:
        px, py = coords_keypad[prev]
        cx, cy = coords_keypad[c]
        dx = cx - px
        dy = cy - py
        hor = lr(dx)
        ver = ud(dy)
        if prev == '<':
            # must go right first
            for r in results:
                r.extend(hor)
                r.extend(ver)
        elif c == '<':
            # must go left last
            for r in results:
                r.extend(ver)
                r.extend(hor)
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

s = 0
for code in codes:
    minlen = 999999999999
    q = set()
    for keys in iternumpad(code):
        for keys1 in iterkeypad(keys):
            for keys2 in iterkeypad(keys1):
                minlen = min(minlen, len(keys2))
                q.add(len(keys2))
    s += int(code.strip('A')) * minlen
    print(q)
print(s)
