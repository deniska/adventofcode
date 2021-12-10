from itertools import count
from hashlib import md5

d = 'cxdnnyjw'
c = 0
p1 = ['_'] * 8
p2 = ['_'] * 8
def out():
    print(''.join(p1), '|', ''.join(p2), end='', flush=True)
out()
for i in count():
    m = md5()
    m.update('{}{}'.format(d, i).encode('ascii'))
    digest = m.hexdigest()
    if digest.startswith('00000'):
        try:
            pos = int(digest[5])
        except ValueError:
            pass
        else:
            if pos < 8 and p2[pos] == '_' :
                p2[pos] = digest[6]
        if c != 8:
            p1[c] = digest[5]
            c += 1
        print('\r', end='')
        out()
        if not '_' in p2:
            break
print()
