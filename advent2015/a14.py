import sys

reindeers = []

def fly(reindeer, seconds):
    speed, duration, rest = reindeer
    full_cycles = seconds // (duration + rest)
    result = full_cycles * speed * duration
    last_cycle = seconds % (duration + rest)
    last_cycle_flight = min(duration, last_cycle)
    result += last_cycle_flight * speed
    return result

with open(sys.argv[1]) as f:
    for line in f:
        parts = line.split()
        speed = int(parts[3])
        duration = int(parts[6])
        rest = int(parts[13])
        reindeers.append((speed, duration, rest))

race_end = 2503

p1 = max(fly(r, race_end) for r in reindeers)
print(p1)

points = [0] * len(reindeers)
for seconds in range(1, race_end + 1):
    res = [fly(r, seconds) for r in reindeers]
    mx = max(res)
    for idx in range(len(reindeers)):
        if res[idx] == mx:
            points[idx] += 1
        
p2 = max(points)
print(p2)
