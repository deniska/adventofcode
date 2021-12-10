import fileinput
import re

def swap_pos(s, x, y):
    x, y = sorted((int(x), int(y)))
    return s[:x] + s[y] + s[x+1:y] + s[x] + s[y+1:]

assert swap_pos('abcde', 4, 0) == 'ebcda'

def swap_let(s, x, y):
    return swap_pos(s, s.index(x), s.index(y))

assert swap_let('ebcda', 'd', 'b') == 'edcba'

def reverse_pos(s, x, y):
    x, y = sorted((int(x), int(y)))
    return s[:x] + s[x:y+1][::-1] + s[y+1:]

assert reverse_pos('edcba', 0, 4) == 'abcde'

def rotate_steps(s, dir, x):
    x = int(x)
    x = x % len(s)
    if dir == 'right':
        x = len(s) - x
    return s[x:] + s[:x]

assert rotate_steps('abcde', 'left', 1) == 'bcdea'
assert rotate_steps('abcd', 'right', 1) == 'dabc'

def move_pos(s, x, y):
    x = int(x)
    y = int(y)
    s = list(s)
    c = s.pop(x)
    s.insert(y, c)
    return ''.join(s)

assert move_pos('bcdea', 1, 4) == 'bdeac'
assert move_pos('bdeac', 3, 0) == 'abdec'

def rotate_pos(s, x):
    i = s.index(x) + 1
    if i > 4:
        i += 1
    return rotate_steps(s, 'right', i)

assert rotate_pos('ecabd', 'd') == 'decab'
assert rotate_pos('hgdcebfa', 'c') == 'ebfahgdc'

mapping = {
        r'swap position (\d+) with position (\d+)': swap_pos,
        r'swap letter (.) with letter (.)': swap_let,
        r'rotate (left|right) (\d+) step': rotate_steps,
        r'rotate based on position of letter (.)': rotate_pos,
        r'reverse positions (\d+) through (\d+)': reverse_pos,
        r'move position (\d+) to position (\d+)': move_pos,
        }

def reverse_rotate_steps(s, dir, i):
    return rotate_steps(s, {'left': 'right', 'right': 'left'}[dir], i)

assert reverse_rotate_steps(rotate_steps('abcde', 'left', 3), 'left', 3) == 'abcde'

def reverse_rotate_pos(s, c):
    # too lazy to think
    for i in range(len(s)):
        s2 = rotate_steps(s, 'left', i)
        if rotate_pos(s2, c) == s:
            return s2

def reverse_move_pos(s, x, y):
    return move_pos(s, y, x)

reverse_mapping = {
        **{v: v for v in mapping.values()},
        rotate_steps: reverse_rotate_steps,
        move_pos: reverse_move_pos,
        rotate_pos: reverse_rotate_pos,
        }

def main():
    s = 'abcdefgh'
    a = ''.join(str(i) for i in range(len(s)))
    inp = []
    for line in fileinput.input():
        inp.append(line)
        for regex, func in mapping.items():
            m = re.match(regex, line)
            if m:
                s = func(s, *m.groups())
                break
        else:
            raise ValueError('"{}" not in the mapping'.format(line.strip()))
    print(s)
    s = 'fbgdceah'
    for line in reversed(inp):
        for regex, func in mapping.items():
            m = re.match(regex, line)
            if m:
                s = reverse_mapping[func](s, *m.groups())
                break
        else:
            raise ValueError('"{}" not in the mapping'.format(line.strip()))
    print(s)

if __name__ == '__main__':
    main()
