import re
import json

def parse(s):
    grp = []
    grp_stack = [grp]
    garbage = False
    skip_next = False
    g = 0
    for c in s:
        if skip_next:
            skip_next = False
            continue
        if c == '!':
            skip_next = True
            continue
        if garbage and c != '>':
            g += 1
            continue
        elif garbage and c == '>':
            garbage = False
            continue
        if c == '{':
            grp = []
            grp_stack[-1].append(grp)
            grp_stack.append(grp)
        elif c == '}':
            grp_stack.pop()
        elif c == '<':
            garbage = True
    return grp_stack[0][0], g

def score(g, i=1):
    return i + sum(score(a, i+1) for a in g)

def main():
    with open('input09.txt') as f:
        s = f.read().strip()
    g, garbage = parse(s)
    print(score(g), garbage)

if __name__ == '__main__':
    main()
