import sys

with open(sys.argv[1]) as f:
    banks = [l.strip() for l in f]

p1 = 0

for bank in banks:
    m = 0
    for i in range(len(bank) - 1):
        a = bank[i]
        for j in range(i+1, len(bank)):
            b = bank[j]
            n = int(f'{a}{b}')
            if n > m:
                m = n
    p1 += m

print(p1)
