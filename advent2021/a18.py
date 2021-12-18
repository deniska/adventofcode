import sys
import re
import json

def conv(line):
    n = re.findall(r'\[|\]|\d+', line)
    for i, c in enumerate(n):
        if c.isdigit():
            n[i] = int(c)
    return n

nums = []
with open(sys.argv[1]) as f:
    for line in f:
        nums.append(conv(line))

def part1(nums):
    s = nums[0]
    for n in nums[1:]:
        s = add(s, n)
    print(pr(s))
    print(magnitude(s))

def part2(nums):
    m = 0
    for n1 in nums:
        for n2 in nums:
            if n1 == n2:
                continue
            a = add(n1, n2)
            m = max(m, magnitude(a))
    print(m)

def magnitude(n):
    j = json.loads(pr(n))
    return magn(j)

def magn(a):
    if isinstance(a, int):
        return a
    return 3*magn(a[0]) + 2*magn(a[1])

def add(a, b):
    s = ['[', *a, *b, ']']
    s = reduce(s)
    return s

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

def pr(num):
    a = []
    prev = None
    for c in num:
        if c != ']' and (isinstance(prev, int) or prev == ']'):
            a.append(',')
        a.append(str(c))
        prev = c
    return ''.join(a)

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

assert explode(conv('[[[[[9,8],1],2],3],4]'))[0] == conv('[[[[0,9],2],3],4]')
assert explode(conv('[7,[6,[5,[4,[3,2]]]]]'))[0] == conv('[7,[6,[5,[7,0]]]]')
assert explode(conv('[[6,[5,[4,[3,2]]]],1]'))[0] == conv('[[6,[5,[7,0]]],3]')
assert explode(conv('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'))[0] == conv('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
assert explode(conv('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'))[0] == conv('[[3,[2,[8,0]]],[9,[5,[7,0]]]]')

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

assert add(conv('[[[[4,3],4],4],[7,[[8,4],9]]]'), conv('[1,1]')) == conv('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

part1(nums)
part2(nums)
