import sys
from collections import defaultdict

def main():
    orbits = {}
    with open(sys.argv[1]) as f:
        for line in f:
            a, b = line.strip().split(')')
            orbits[b] = a
    print(part1(orbits))
    print(part2(orbits))

def part1(orbits):
    c = 0
    for b in orbits:
        c += count(orbits, b)
    return c

def part2(orbits):
    you_path = path(orbits, 'YOU')
    san_path = path(orbits, 'SAN')
    disjoint = you_path ^ san_path
    print(disjoint)
    return len(disjoint) - 2

def count(orbits, b):
    c = 0
    while b != 'COM':
        c += 1
        b = orbits[b]
    return c

def path(orbits, b):
    p = set()
    while b != 'COM':
        p.add(b)
        b = orbits[b]
    return p

if __name__ == '__main__':
    main()
