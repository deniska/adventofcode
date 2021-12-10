import sys

with open(sys.argv[1]) as f:
    ns = [int(n) for n in f.read().strip().split(',')]

def sim(ns, days):
    fish = [0] * 9
    for n in ns:
        fish[n] += 1
    for day in range(days):
        f0 = fish[0]
        fish[0] = fish[1]
        fish[1] = fish[2]
        fish[2] = fish[3]
        fish[3] = fish[4]
        fish[4] = fish[5]
        fish[5] = fish[6]
        fish[6] = fish[7] + f0
        fish[7] = fish[8]
        fish[8] = f0
    return sum(fish)

#print(sim(ns, 80))
#print(sim(ns, 256))
sim(ns, 9999999)
