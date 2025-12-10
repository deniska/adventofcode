import sys
import itertools
import z3

lights = []
buttons = []
buttons_ids = []
joltages = []

with open(sys.argv[1]) as f:
    for line in f:
        mlights, *mbuttons, mjoltage = line.split()
        mlights = int(mlights.strip('][').replace('.', '0').replace('#', '1')[::-1], 2)
        lights.append(mlights)
        bs = []
        bsi = []
        for mbutton in mbuttons:
            b = 0
            bi = []
            for mb in mbutton.strip(')(').split(','):
                b |= 1 << int(mb)
                bi.append(int(mb))
            bs.append(b)
            bsi.append(bi)
        buttons.append(bs)
        buttons_ids.append(bsi)
        joltages.append(list(map(int, mjoltage.strip('}{').split(','))))

p1 = 0
p2 = 0

def solve_p2(joltages, buttons):
    ks = z3.IntVector('k', len(buttons))
    eqs = []
    eqs.extend(k >= 0 for k in ks)
    for j, jlt in enumerate(joltages):
        eq = []
        for i, btn in enumerate(buttons):
            if j in btn:
                eq.append(ks[i])
        eqs.append(sum(eq) == jlt)
    sol = z3.Solver()
    sol.add(eqs)
    while True:
        if sol.check() == z3.unsat:
            break
        model = sol.model()
        s = sum(model[k].as_long() for k in ks)
        sol.add(sum(ks) < s)
    return s

for light, btns, btnsi, joltage in zip(lights, buttons, buttons_ids, joltages):
    q = 999999
    for presses in itertools.product(*len(btns)*[range(2)]):
        r = 0
        for press, btn in zip(presses, btns):
            if press:
                r ^= btn
        if r != light:
            continue
        q = min(q, sum(presses))
    p1 += q
    w = solve_p2(joltage, btnsi)
    p2 += w

print(p1)
print(p2)
