import re
import sys

cnt = 0
cnt2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        a, b, char, pw = re.match(r'(\d+)-(\d+) (.): (.+)', line).groups()
        a = int(a)
        b = int(b)
        if a <= pw.count(char) <= b:
            cnt += 1
        if (pw[a-1] + pw[b-1]).count(char) == 1:
            cnt2 += 1

print(cnt)
print(cnt2)
