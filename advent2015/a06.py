import sys
import re

def part1():
    lamps = [False] * 1000000
    with open(sys.argv[1]) as f:
        for line in f:
            x1, y1, x2, y2 = [int(x) for x in re.findall(r'\d+', line)]
            if line.startswith('toggle'):
                toggle(lamps, x1, y1, x2, y2)
            elif line.startswith('turn on'):
                set_lamps(lamps, x1, y1, x2, y2, True)
            elif line.startswith('turn off'):
                set_lamps(lamps, x1, y1, x2, y2, False)
    print(lamps.count(True))

def part2():
    lamps = [0] * 1000000
    with open(sys.argv[1]) as f:
        for line in f:
            x1, y1, x2, y2 = [int(x) for x in re.findall(r'\d+', line)]
            if line.startswith('toggle'):
                add_val(lamps, x1, y1, x2, y2, 2)
            elif line.startswith('turn on'):
                add_val(lamps, x1, y1, x2, y2, 1)
            elif line.startswith('turn off'):
                add_val(lamps, x1, y1, x2, y2, -1)
    print(sum(lamps))

def toggle(lamps, x1, y1, x2, y2):
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            lamps[j + i*1000] = not lamps[j + i*1000]

def set_lamps(lamps, x1, y1, x2, y2, v):
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            lamps[j + i*1000] = v

def add_val(lamps, x1, y1, x2, y2, v):
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            lamps[j + i*1000] = max(0, lamps[j + i*1000] + v)

part1()
part2()
