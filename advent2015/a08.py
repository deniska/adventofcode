import ast
import sys

tot = 0
tot1 = 0
tot2 = 0

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        tot += len(line)
        tot1 += len(ast.literal_eval(line))
        tot2 += len(line.replace('\\', '\\\\').replace('"', '\\"')) + 2

p1 = tot - tot1
print(p1)

p2 = tot2 - tot
print(p2)
