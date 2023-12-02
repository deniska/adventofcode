import re
import sys

text_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

s = 0
with open(sys.argv[1]) as f:
    for line in f:
        digits = re.findall(r'\d', line)
        num = int(digits[0] + digits[-1])
        s += num

print(s)

def find_digits(s):
    first = None
    for i in range(len(s)):
        if s[i].isdigit():
            first = s[i]
        else:
            for k, v in text_digits.items():
                if s.startswith(k, i):
                    first = v
        if first is not None:
            break
    last = None
    for i in range(len(s)-1, -1, -1):
        if s[i].isdigit():
            last = s[i]
            break
        else:
            for k, v in text_digits.items():
                if s.endswith(k, 0, i):
                    last = v
        if last is not None:
            break
    return first, last

s = 0
with open(sys.argv[1]) as f:
    for line in f:
        a, b = find_digits(line)
        num = int(f'{a}{b}')
        s += num
print(s)
