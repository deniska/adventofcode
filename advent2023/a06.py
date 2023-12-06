import sys

with open(sys.argv[1]) as f:
    times = [int(x) for x in next(f).split(':')[1].split()]
    distances = [int(x) for x in next(f).split(':')[1].split()]

c = 1
for time, distance in zip(times, distances):
    n = 0
    for t in range(1, time - 1):
        d = t * (time - t)
        if d > distance:
            n += 1
    c *= n
print(c)

c = 1
time = int(''.join(str(x) for x in times))
distance = int(''.join(str(x) for x in distances))
n = 0
for t in range(1, time - 1):
    d = t * (time - t)
    if d > distance:
        n += 1
print(n)
