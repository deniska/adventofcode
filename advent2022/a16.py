import sys
import functools

flow_rates = {}
connections = {}

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        parts = line.split()
        lead_to = [p.strip(', ') for p in parts[9:]]
        valve_name = parts[1]
        flow_rate = int(parts[4].strip(';').removeprefix('rate='))
        flow_rates[valve_name] = flow_rate
        connections[valve_name] = lead_to

cache = {} # at, open_valves => score, minutes_left
@functools.cache
def search(score=0, at='AA', minutes_left=30, open_valves=frozenset()):
    if cached := cache.get((at, open_valves)):
        old_score, old_minutes_left = cached
        if old_score > score and old_minutes_left > minutes_left:
            # something else is strictly better
            return 0
    if minutes_left <= 0:
        return score
    flow_rate = flow_rates[at]
    lead_to = connections[at]
    max_score = 0
    for valve in lead_to:
        if flow_rate > 0 and at not in open_valves and minutes_left > 1:
            # with opening the valve
            max_score = max(max_score, search(score+flow_rate * (minutes_left-1), valve, minutes_left - 2, open_valves | {at}))
        # without opening the valve
        max_score = max(max_score, search(score, valve, minutes_left-1, open_valves))
    cache[at, open_valves] = score, minutes_left
    return max_score

print(search())
