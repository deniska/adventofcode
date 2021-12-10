import sys
import statistics

lines = []
with open(sys.argv[1]) as f:
    for line in f:
        lines.append(line.strip())

pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
        }

scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        }

scores2 = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
        }

def check_line(line):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(c)
        else:
            op = stack.pop()
            if pairs[op] != c:
                return scores[c], 0
    s = 0
    while stack:
        c = stack.pop()
        s *= 5
        s += scores2[c]
    return 0, s

p1 = 0
p2 = []
for line in lines:
    a = check_line(line)
    p1 += a[0]
    if a[1] > 0:
        p2.append(a[1])
print(p1)
print(int(statistics.median(p2)))
