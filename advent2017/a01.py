with open('input01.txt') as f:
    digits = [int(a) for a in f.read().strip()]

print(sum(d for d, n in zip(digits, [*digits[1:], digits[0]]) if d == n))
x = len(digits) // 2
print(sum(d for d, n in zip(digits, [*digits[x:], *digits[:x]]) if d == n))
