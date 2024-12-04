import sys
import itertools

def is_nice(s):
    if any(x in s for x in ('ab', 'cd', 'pq', 'xy')):
        return False
    vowels = 0
    for v in 'aeiou':
        vowels += s.count(v)
    if vowels < 3:
        return False
    twice = False
    for a, b in itertools.pairwise(s):
        if a == b:
            twice = True
    if not twice:
        return False
    return True

def is_nice2(s):
    for a, b in itertools.pairwise(s):
        if s.count(a+b) >= 2:
            break
    else:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            break
    else:
        return False
    return True

assert is_nice('ugknbfddgicrmopn')
assert is_nice('aaa')
assert not is_nice('jchzalrnumimnmhp')
assert not is_nice('haegwjzuvuyypxyu')
assert not is_nice('dvszwmarrgswjxmb')

nice = 0
nice2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if is_nice(line):
            nice += 1
        if is_nice2(line):
            nice2 += 1
print(nice)
print(nice2)
