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
for tile, borders in tiles.items():
    c = 0
    for other_tile, other_borders in tiles.items():
        for border in borders:
            if border in other_borders:
                c += 1
    if c == 12:
        m *= tile

print(m)
