import sys
import collections

with open(sys.argv[1]) as f:
    data = f.read()

nums1 = []
nums2 = []
for line in data.split('\n'):
    if not line:
        continue
    n1, n2 = line.split()
    n1 = int(n1)
    n2 = int(n2)
    nums1.append(n1)
    nums2.append(n2)

snums1 = sorted(nums1)
snums2 = sorted(nums2)
d = 0

for n1, n2 in zip(snums1, snums2):
    d += abs(n1 - n2)

print(d)

s = 0
counts = collections.Counter(nums2)
for n1 in nums1:
    s += n1 * counts[n1]

print(s)
