fuel = 0
with open('input01.txt') as f:
    for line in f:
        f = int(line.strip())
        while f > 0:
            f = f // 3 - 2
            if f > 0:
                fuel += f
print(fuel)
