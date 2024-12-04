import sys

with open(sys.argv[1]) as f:
    data = f.read()

print(data.count('(') - data.count(')'))

f = 0

for i, c in enumerate(data, start=1):
    if c == '(':
        f += 1
    elif c == ')':
        f -= 1
    if f == -1:
        print(i)
        break
