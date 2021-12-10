step = 354
buf = [0]
coord = 0
for num in range(1, 2018):
    coord = (coord + step) % len(buf) + 1
    buf.insert(coord, num)
print(buf[buf.index(2017) + 1])

zeropos = 0
for num in range(1, 50000001):
    coord = (coord + step) % num + 1
    if zeropos >= coord:
        zeropos += 1
    elif coord - zeropos == 1:
        afterzero = num
print(afterzero)
