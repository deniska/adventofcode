from collections import defaultdict
import re

regs = defaultdict(int)
code = []
with open('input08.txt') as f:
    for line in f:
        m = re.match(r'(\w+) (dec|inc) (-?\d+) if (\w+) (.+)', line)
        op = {'dec': '-=', 'inc': '+='}[m[2]]
        code.append(f'if regs["{m[4]}"] {m[5]}: regs["{m[1]}"] {op} {m[3]}')
        code.append('mx = max(*regs.values(), mx)')

ns = {'regs': regs, 'mx': 0}
exec('\n'.join(code), ns)
print(max(regs.values()))
print(ns['mx'])
