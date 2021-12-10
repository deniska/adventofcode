from itertools import islice

def gen(val, factor, i=1):
    while True:
        val *= factor
        val %= 2147483647
        if val % i == 0:
            yield val

def go(g1, g2, count):
    c = 0
    for a, b in islice(zip(g1, g2), count):
        if a & 0xffff == b & 0xffff:
            c += 1
    return c

def part1():
    g1 = gen(699, 16807)
    g2 = gen(124, 48271)
    return go(g1, g2, 40000000)

def part2():
    g1 = gen(699, 16807, 4)
    g2 = gen(124, 48271, 8)
    return go(g1, g2, 5000000)

if __name__ == '__main__':
    print(part1())
    print(part2())
