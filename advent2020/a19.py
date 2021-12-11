import sys
import re


def main():
    rules = {}
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            idx, rule = line.split(':')
            idx = int(idx)
            rule = rule.split()
            for i, r in enumerate(rule):
                if r.isdigit():
                    rule[i] = int(r)
            rules[idx] = rule
        regex = build_regex(0, rules) + '$'
        regex2 = build_regex(0, rules, part2=True) + '$'
        c = 0
        c2 = 0
        for line in f:
            line = line.strip()
            if re.match(regex, line):
                c += 1
            if re.match(regex2, line):
                c2 += 1
    print(c)
    print(c2)


def build_regex(idx, rules, part2=False):
    parts = []
    if part2:
        if idx == 8:
            parts.append('(')
            rg42 = build_regex(42, rules, part2)
            parts.append(rg42)
            parts.append(')+')
            return ''.join(parts)
        elif idx == 11:
            rg42 = build_regex(42, rules, part2)
            rg31 = build_regex(31, rules, part2)
            for i in range(1, 30):
                parts.append('(')
                for _ in range(i):
                    parts.append('(')
                    parts.append(rg42)
                    parts.append(')')
                for _ in range(i):
                    parts.append('(')
                    parts.append(rg31)
                    parts.append(')')
                parts.append(')')
                parts.append('|')
            parts.pop()
            return ''.join(parts)
    rule = rules[idx]
    for r in rule:
        if r == '|':
            parts.append(r)
        elif isinstance(r, int):
            parts.append('(')
            parts.append(build_regex(r, rules, part2))
            parts.append(')')
        else:
            parts.append(r.strip('"'))
    return ''.join(parts)

if __name__ == '__main__':
    main()
