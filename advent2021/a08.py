import sys
import itertools

segment_digits = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
        }

with open(sys.argv[1]) as f:
    lines = f.readlines()

c = 0
for line in lines:
    out = line.split('|')[1]
    digits = out.split()
    for d in digits:
        ld = len(d)
        if ld in (2, 3, 4, 7):
            c += 1

print(c)
all_segments = 'abcdefg'

c = 0
for line in lines:
    digits, out = line.split('|')
    digits = digits.split()
    out = out.split()
    for p in itertools.permutations(all_segments):
        tr = str.maketrans(all_segments, ''.join(p))
        s = set()
        for d in digits:
            segments = ''.join(sorted(d.translate(tr)))
            num = segment_digits.get(segments)
            if num is not None:
                s.add(num)
        if len(s) == 10:
            break
    ds = 0
    for digit in out:
        ds = ds*10 + segment_digits[''.join(sorted(digit.translate(tr)))]
    c += int(ds)

print(c)
