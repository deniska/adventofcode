import sys

lines = []
with open(sys.argv[1]) as f:
    for line in f:
        lines.append(line.strip())

def check(lines, x, y):
    idx = 0
    cnt = 0
    line_idx = 0
    while line_idx < len(lines):
        line = lines[line_idx]
        if line[idx % len(line)] == '#':
            cnt += 1
        idx += y
        line_idx += x
    return cnt

print(check(lines, 1, 3))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
p = 1
for y, x in slopes:
    p *= check(lines, x, y)
print(p)
