import sys
import pathlib
import re
import itertools

lines = pathlib.Path(sys.argv[1]).read_text().strip().split('\n')

cmds = []

for line in lines:
    if line.startswith('mask'):
        mask = line[-36:]
        cmds.append(('mask', mask))
    else:
        m = re.match(r'mem\[(\d+)\] = (\d+)', line)
        cmds.append(('mem', int(m[1]), int(m[2])))

mem = {}
for cmd in cmds:
    if cmd[0] == 'mask':
        mask = cmd[1]
        and_mask = int(mask.replace('X', '1'), 2)
        or_mask = int(mask.replace('X', '0'), 2)
    elif cmd[0] == 'mem':
        addr = cmd[1]
        val = cmd[2]
        mem[addr] = val & and_mask | or_mask
print(sum(mem.values()))

def iter_floating(bits):
    for vals in itertools.product(*([-2**i, 2**i] for i in bits)):
        and_mask = 0xFFFFFFFFF
        or_mask = 0
        for val in vals:
            if val > 0:
                or_mask |= val
            else:
                and_mask &= ~abs(val)
        yield and_mask, or_mask

mem = {}
for cmd in cmds:
    if cmd[0] == 'mask':
        mask = cmd[1]
        float_bits = [i for i, b in enumerate(mask[::-1]) if b == 'X']
        or_mask = int(mask.replace('X', '0'), 2)
    elif cmd[0] == 'mem':
        addr = cmd[1]
        val = cmd[2]
        for float_and, float_or in iter_floating(float_bits):
            mem[addr & float_and | float_or | or_mask] = val
print(sum(mem.values()))
