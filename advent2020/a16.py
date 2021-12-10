import sys
import re

valid_ranges = []
field_ranges = {}
field_valid_pos = {}
tickets = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        m = re.match(r'([^:]+): (\d+)-(\d+) or (\d+)-(\d+)', line)
        r1 = range(int(m[2]), int(m[3])+1)
        r2 = range(int(m[4]), int(m[5])+1)
        valid_ranges.append(r1)
        valid_ranges.append(r2)
        field_ranges[m[1]] = [r1, r2]
    next(f)
    my_ticket = [int(i) for i in next(f).strip().split(',')]
    for field in field_ranges:
        field_valid_pos[field] = set(range(len(my_ticket)))
    next(f)
    next(f)
    for line in f:
        line = line.strip()
        tickets.append([int(i) for i in line.split(',')])

s = 0
valid_tickets = []
for ticket in tickets:
    is_valid = True
    for num in ticket:
        for r in valid_ranges:
            if num in r:
                break
        else:
            s += num
            is_valid = False
    if is_valid:
        valid_tickets.append(ticket)
print(s)


for ticket in valid_tickets:
    for i, n in enumerate(ticket):
        for field, ranges in field_ranges.items():
            valid = False
            for r in ranges:
                if n in r:
                    valid = True
                    break
            if not valid:
                field_valid_pos[field] -= {i}

field_index = {}
while len(field_index) < len(field_valid_pos):
    for field, possible in field_valid_pos.items():
        if len(possible) == 1:
            v = possible.pop()
            field_index[field] = v
            for f in field_valid_pos.values():
                f -= {v}

c = 1
for field, idx in field_index.items():
    if 'departure' not in field:
        continue
    c *= my_ticket[idx]
print(c)
