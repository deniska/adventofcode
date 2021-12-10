import math

def conv(s):
    lines = s.strip().split('\n')
    numlines = []
    for line in lines:
        numlines.append([int(i) for i in line.split()])
    return numlines

def chksm(s):
    numlines = conv(s)
    return sum(max(line)-min(line) for line in numlines)

def chksm2(s):
    numlines = conv(s)
    return sum(divpair(line) for line in numlines)

def divpair(line):
    for x in line:
        for y in line:
            if x == y:
                continue
            if math.gcd(x, y) == y:
                return x // y

assert chksm('''5 1 9 5
7 5 3
2 4 6 8''') == 18

assert chksm2('''5 9 2 8
9 4 7 3
3 8 6 5''') == 9

def main():
    with open('input02.txt') as f:
        s = f.read()
    print(chksm(s))
    print(chksm2(s))

if __name__ == '__main__':
    main()
