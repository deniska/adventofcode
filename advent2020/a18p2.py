import sys
import re

def main():
    s = 0
    with open(sys.argv[1]) as f:
        for line in f:
            a = list(reversed(re.findall(r'\d+|[*+()]', line)))
            s += math(a)
    print(s)

# thanks to shunting yard from https://gist.github.com/ollybritton/3ecdd2b28344b0b25c547cbfcb807ddc
def math(expr):
    out = []
    ops = []
    while expr:
        tok = expr.pop()
        if tok.isdigit():
            out.append(int(tok))
        elif tok in '+*':
            while True:
                if not ops:
                    break
                flag = False
                if ops[-1] not in '()':
                    if ops[-1] == '+' and tok == '*':
                        flag = True
                flag = flag and ops[-1] != '('
                if not flag:
                    break
                out.append(ops.pop())
            ops.append(tok)
        elif tok == '(':
            ops.append(tok)
        elif tok == ')':
            while True:
                if not ops:
                    break
                if ops[-1] == '(':
                    break
                out.append(ops.pop())
            if ops and ops[-1] == '(':
                ops.pop()
    out += reversed(ops)
    stack = []
    for a in out:
        if a == '*':
            stack.append(stack.pop() * stack.pop())
        elif a == '+':
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(a)
    return stack[0]

if __name__ == '__main__':
    main()
