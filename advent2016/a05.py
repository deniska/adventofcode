from itertools import count
from hashlib import md5

def out(p1, p2):
    print(''.join(p1), '|', ''.join(p2), end='', flush=True)

def main():
    d = b'cxdnnyjw'
    base = md5(d)
    c = 0
    c1 = 0
    p1 = ['_'] * 8
    p2 = ['_'] * 8
    out(p1, p2)
    i = 0
    for i in count():
        m = base.copy()
        m.update(str(i).encode('ascii'))
        digest = m.hexdigest()
        if digest.startswith('00000'):
            dig5 = digest[5]
            if dig5 in '01234567':
                pos = int(dig5)
                if p2[pos] == '_' :
                    p2[pos] = digest[6]
                    c1 += 1
            if c != 8:
                p1[c] = dig5
                c += 1
            print('\r', end='')
            out(p1, p2)
            if c1 == 8:
                break
    print()

main()
