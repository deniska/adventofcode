from collections import deque
route_raw = 'R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3'

directions = deque([0+1j, 1+0j, 0-1j, -1+0j])

locations = set()

route = [r.strip(',') for r in route_raw.split()]
coord = 0+0j
found_visited = False
for s in route:
    rotation, distance = s[0], int(s[1:])
    directions.rotate({'R': 1, 'L': -1}[rotation])
    direction = directions[0]
    if not found_visited:
        for d in range(distance):
            loc = coord + direction * d
            if loc in locations:
                print('Visited more than once:', 
                        abs(loc.real) + abs(loc.imag))
                found_visited = True
            locations.add(loc)
    coord += directions[0] * distance

print(abs(coord.real) + abs(coord.imag))
