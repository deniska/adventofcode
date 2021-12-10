import sys

def testnum(i):
    digits = str(i)
    same = False
    exactdouble = False
    monotone = True
    for x, y in zip(digits, digits[1:]):
        if digits.count(x) >= 2:
            same = True
        if digits.count(x) == 2:
            exactdouble = True
        if x > y:
            monotone = False
            break
    return same and monotone, exactdouble and monotone

def main():
    a, b = sys.argv[1].split('-')
    a = int(a)
    b = int(b)
    c1 = 0
    c2 = 0
    for i in range(a, b+1):
        p1, p2 = testnum(i)
        if p1:
            c1 += 1
        if p2:
            c2 += 1
    print(c1)
    print(c2)

if __name__ == '__main__':
    main()
