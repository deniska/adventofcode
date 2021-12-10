fuel = 0
with open('input01.txt') as f:
    for line in f:
        fuel += int(line.strip()) // 3 - 2
print(fuel)
