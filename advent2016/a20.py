from pprint import pprint
import fileinput

def find_lowest(ranges):
    r = sorted(ranges)
    i = 0
    for low, high in r:
        if low <= i and high >= i:
            i = high+1
        elif low > i:
            break
    return i

def count(ranges, m=4294967295):
    ranges = sorted(ranges)
    merged = [ranges[0]]
    for low, high in ranges[1:]:
        if merged[-1][1] >= low-1:
            if high > merged[-1][1]:
                merged[-1] = merged[-1][0], high
        else:
            merged.append((low, high))
    c = 0
    for (low1, high1), (low2, high2) in zip(merged, merged[1:]):
        c += low2 - high1 - 1
    c += m - merged[-1][1]
    return c

assert(count([(5, 8), (0, 2), (4, 7)], 9) == 2)
assert(count([(0, 1), (0, 2), (2, 5), (7, 8)], 10) == 3)
assert(count([(0, 3), (7, 8)], 10) == 5)
ranges = []
for line in fileinput.input():
    line = line.strip()
    low, high = line.split('-')
    low = int(low)
    high = int(high)
    ranges.append((low, high))

print(find_lowest(ranges))
print(count(ranges))
