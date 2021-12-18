import sys
import re
import json

class SnailfishNumber:

    def __init__(self, num):
        self.num = num

    def __add__(self, another):
        s = ['[', *self.num, *another.num, ']']
        s = reduce(s)
        return type(self)(s)

    def __str__(self):
        a = []
        prev = None
        for c in self.num:
            if c != ']' and (isinstance(prev, int) or prev == ']'):
                a.append(',')
            a.append(str(c))
            prev = c
        return ''.join(a)

    def magnitude(self):
        j = json.loads(str(self))
        return magn(j)

    @classmethod
    def from_string(cls, s):
        n = re.findall(r'\[|\]|\d+', s)
        for i, c in enumerate(n):
            if c.isdigit():
                n[i] = int(c)
        return cls(n)


nums = []
with open(sys.argv[1]) as f:
    for line in f:
        nums.append(SnailfishNumber.from_string(line))

def part1(nums):
    s = nums[0]
    for n in nums[1:]:
        s += n
    print(s)
    print(s.magnitude())

def part2(nums):
    m = 0
    for n1 in nums:
        for n2 in nums:
            if n1 == n2:
                continue
            a = n1 + n2
            m = max(m, a.magnitude())
    print(m)

def magn(a):
    if isinstance(a, int):
        return a
    return 3*magn(a[0]) + 2*magn(a[1])

def reduce(num):
    while True:
        num, exploded = explode(num)
        if exploded:
            continue
        num, was_split = split(num)
        if was_split:
            continue
        break
    return num

def explode(num):
    lvl = 0
    pos = None
    for i, c in enumerate(num):
        if c == '[':
            lvl += 1
        elif c == ']':
            lvl -= 1
        if lvl == 5 and isinstance(num[i+1], int) and isinstance(num[i+2], int):
            pos = i
            break
    if pos is not None:
        left = num[pos+1]
        right = num[pos+2]
        part1 = num[:pos]
        part2 = num[pos+4:]
        dpos = None
        for i, c in enumerate(part1):
            if isinstance(c, int):
                dpos = i
        if dpos is not None:
            part1[dpos] += left
        for i, c in enumerate(part2):
            if isinstance(c, int):
                part2[i] += right
                break
        n = [*part1, 0, *part2]
        return n, True
    return num, False

def split(num):
    n = []
    was_split = False
    for c in num:
        if not was_split and isinstance(c, int) and c >= 10:
            n.append('[')
            n.append(c // 2)
            n.append((c+1) // 2)
            n.append(']')
            was_split = True
        else:
            n.append(c)
    return n, was_split

part1(nums)
part2(nums)
