def main(s, length):
    tbl = str.maketrans('01', '10')
    while len(s) < length:
        s += '0' + s.translate(tbl)[::-1]
    s = s[:length]
    while True:
        checksum = ''
        for c1, c2 in zip(s[::2], s[1::2]):
            if c1 == c2:
                checksum += '1'
            else:
                checksum += '0'
        s = checksum
        if len(s) % 2 == 1:
            break
    return s

s = '00111101111101000'
length = 272

assert main('10000', 20) == '01100'

print(main(s, length))
print(main(s, 35651584))
