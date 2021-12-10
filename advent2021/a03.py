import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split()

pos_cnt = [0] * len(lines[0])
for line in lines:
    for i, c in enumerate(line):
        if c == '1':
            pos_cnt[i] += 1

cnt = len(lines)
gamma = ''.join('1' if q > cnt / 2 else '0' for q in pos_cnt)
gamma = int(gamma, 2)

eps = ''.join('1' if q < cnt / 2 else '0' for q in pos_cnt)
eps = int(eps, 2)

print(gamma * eps)

filtered = lines
for bit_n in range(len(lines[0])):
    cnt_1 = 0
    for line in filtered:
        if line[bit_n] == '1':
            cnt_1 += 1
    if cnt_1 >= len(filtered) / 2:
        c = '1'
    else:
        c = '0'
    filtered = [a for a in filtered if a[bit_n] == c]

oxy = int(filtered[0], 2)

filtered = lines
for bit_n in range(len(lines[0])):
    cnt_1 = 0
    for line in filtered:
        if line[bit_n] == '1':
            cnt_1 += 1
    if cnt_1 < len(filtered) / 2:
        c = '1'
    else:
        c = '0'
    filtered = [a for a in filtered if a[bit_n] == c]
    if len(filtered) == 1:
        break

co2 = int(filtered[0], 2)
print(co2 * oxy)
