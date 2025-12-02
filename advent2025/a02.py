import sys

with open(sys.argv[1]) as f:
    s = f.read().strip()

ranges = []
for r in s.split(','):
    a, b = r.split('-')
    ranges.append((int(a), int(b)))

p1 = 0
p2 = 0
for a, b in ranges:
    for q in range(a, b+1):
        s = str(q)
        l = len(s)
        for part_count in range(2, l+1):
            if l % part_count != 0:
                continue
            part_len = l // part_count
            ss = s[:part_len]
            for part_idx in range(1, part_count):
                if s[part_len*part_idx:part_len*(part_idx+1)] != ss:
                    break
            else:
                if part_count == 2:
                    p1 += q
                p2 += q
                break

print(p1)
print(p2)
