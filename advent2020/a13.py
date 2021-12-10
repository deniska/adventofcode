import sys
import itertools

with open(sys.argv[1]) as f:
    ts = int(f.readline())
    bus_data = [(int(s), i)
            for i, s in enumerate(f.readline().split(','))
            if s != 'x']

buses = [a[0] for a in bus_data]
next_times = {ts // b * b + b: b for b in buses}
dep_time, bus = min(next_times.items())
print(bus * (dep_time - ts))

sol = 0
inc = buses[0]

for bus, idx in bus_data[1:]:
    c = (bus - idx) % bus
    while True:
        if sol % bus == c:
            inc *= bus
            break
        sol += inc
print(sol)

