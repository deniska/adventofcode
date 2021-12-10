from collections import Counter

counters = [Counter() for _ in range(8)]
with open('input6.txt') as f:
    for line in f:
        for counter, char in zip(counters, line):
            counter.update(char)

print(''.join(c.most_common(1)[0][0] for c in counters))
print(''.join(c.most_common()[-1][0] for c in counters))
