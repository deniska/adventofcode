import sys
import re

def main():
    s = 0
    with open(sys.argv[1]) as f:
        for line in f:
            a = list(reversed(re.findall(r'\d+|[*+()]', line)))
            s += math(a)
    print(s)

def math(expr):
    r = expr.pop()
    if r == '(':
        r = math(expr)
    else:
        r = int(r)
    while True:
        if not expr:
            return r
        op = expr.pop()
        if op == ')':
            return r
        n = expr.pop()
        if n == '(':
            n = math(expr)
        else:
            n = int(n)
        if op == '*':
            r *= n
        elif op == '+':
            r += n
        else:
            raise Exception('No')


if __name__ == '__main__':
    main()
