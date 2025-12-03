import sys

with open(sys.argv[1]) as f:
    banks = [l.strip() for l in f]

def num(bank, indices):
    return int(''.join(bank[i] for i in indices))

def solve(bank, cnt):
    result = 0
    for bank in banks:
        m = 0
        indices = list(range(len(bank) - cnt, len(bank)))
        prev_index = -1
        for index_index, index in enumerate(indices):
            new_indices = indices.copy()
            for i in range(index, prev_index, -1):
                new_indices[index_index] = i
                if (new_m := num(bank, new_indices)) >= m:
                    indices = new_indices.copy()
                    m = new_m
            prev_index = indices[index_index]
        result += m
    return result

p1 = solve(banks, 2)
p2 = solve(banks, 12)

print(p1)
print(p2)
