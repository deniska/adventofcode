import sys

with open(sys.argv[1]) as f:
    ns = [int(n) for n in f.read().strip().split(',')]

def sim(ns, days):
    fish = [0] * 9
    for n in ns:
        fish[n] += 1
    for day in range(days):
        fish = [
                fish[1], #0
                fish[2], #1
                fish[3], #2
                fish[4], #3
                fish[5], #4
                fish[6], #5
                fish[7] + fish[0], #6
                fish[8], #7
                fish[0], #8
                ]
    return sum(fish)

print(sim(ns, 80))
print(sim(ns, 256))
