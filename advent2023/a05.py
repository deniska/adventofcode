import sys
from dataclasses import dataclass
from collections import defaultdict

def main():
    maps = defaultdict(Map)
    with open(sys.argv[1]) as f:
        seeds = [int(x) for x in next(f).split(': ')[1].split()]
        next(f)
        current_map = None
        for line in f:
            line = line.strip()
            if not line:
                continue
            elif 'map' in line:
                current_map = line.split()[0]
            else:
                nums = [int(x) for x in line.split()]
                maps[current_map].add_range(Range(*nums))
    location = 99999999999999999999
    for seed in seeds:
        for map_name in map_names:
            seed = maps[map_name].map(seed)
        if seed < location:
            location = seed
    print(location)

    location = 99999999999999999999
    for seed_start, seed_cnt in zip(seeds[0::2], seeds[1::2]):
        for seed in range(seed_start, seed_start+seed_cnt+1):
            for map_name in map_names:
                seed = maps[map_name].map(seed)
            if seed < location:
                location = seed
    print(location)


map_names = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location',
]


@dataclass
class Range:
    dst: int
    src: int
    length: int

class Map:
    def __init__(self):
        self.ranges = []
    
    def add_range(self, r):
        self.ranges.append(r)

    def map(self, n):
        for r in self.ranges:
            if r.src <= n <= r.src + r.length:
                return n + r.dst - r.src
        return n

if __name__ == '__main__':
    main()
