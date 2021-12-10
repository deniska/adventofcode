from collections import deque
lengths = [88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205]
def round(nums, lengths, skip=0, cur=0):
    for a in lengths:
        cur += a + skip
        ns = []
        for i in range(a):
            ns.append(nums.popleft())
        nums.extendleft(ns)
        nums.rotate(-a-skip)
        skip += 1
    return nums, cur, skip

def hash2(s):
    nums2 = deque(range(256))
    lengths = list(s.encode('ascii'))
    lengths.extend([17, 31, 73, 47, 23])

    skip = 0
    cur = 0
    for _ in range(64):
        nums2, cur, skip = round(nums2, lengths, skip, cur)
    nums2.rotate(cur)
    dense = []
    for i in range(16):
        n = nums2[i*16]
        for j in range(1, 16):
            n ^= nums2[i*16+j]
        dense.append(n)
    return bytes(dense).hex()

if __name__ == '__main__':
    part1, cur, _ = round(deque(range(256)), lengths)
    part1.rotate(cur)
    print(part1[0] * part1[1])
    print(hash2('88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205'))
