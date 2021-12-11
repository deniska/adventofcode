import sys
import re

with open(sys.argv[1]) as f:
    s = f.read().strip()

tiles = {}
for tile_s in s.split('\n\n'):
    lines = tile_s.split('\n')
    tile_id = int(re.search(r'\d+', lines[0])[0])
    borders = [
            lines[1],
            lines[-1],
            ''.join(l[0] for l in lines[1:]),
            ''.join(l[-1] for l in lines[1:]),
            ]
    borders += [b[::-1] for b in borders]
    tiles[tile_id] = borders

m = 1
can_connect_to = {}
indices = {}
for tile, borders in tiles.items():
    can_connect_to[tile] = set()
    for other_tile, other_borders in tiles.items():
        if tile == other_tile:
            continue
        for i, border in enumerate(borders):
            try:
                j = other_borders.index(border)
                can_connect_to[tile].add(other_tile)
                indices[tile, other_tile] = i, j
            except ValueError:
                pass
    if len(can_connect_to[tile]) == 2:
        m *= tile

print(m)
print(can_connect_to)
print(indices)
