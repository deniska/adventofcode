from collections import deque

def part1_deque(count):
    elves = deque(range(1, count+1))
    while len(elves) > 1:
        del elves[1]
        elves.rotate(-1)
    return elves[0]

def part1_iter(count):
    a = 1
    b = 1
    while a < count:
        b += 2
        a += 1
        if b > a:
            b = 1
    return b

def part2_deque(count):
    elves = deque(range(1, count+1))
    while len(elves) > 1:
        del elves[len(elves) // 2]
        elves.rotate(-1)
    return elves[0]

def part2_iter(count):
    a = 2
    b = 1
    while a < count:
        if b >= a:
            b = 0
        if b < (a+1)//2:
            b += 1
        else:
            b += 2
        a += 1
    return b

N = 3017957
for i in range(2, 1000):
    assert part1_deque(i) == part1_iter(i)
    assert part2_deque(i) == part2_iter(i)

print(part1_iter(N))
print(part2_iter(N))
