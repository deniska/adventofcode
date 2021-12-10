import hashlib

hex_open = 'bcdef'
def open_doors(code, path):
    m = hashlib.md5((code+path).encode('ascii'))
    d = m.hexdigest()
    if d[0] in hex_open:
        yield 'U'
    if d[1] in hex_open:
        yield 'D'
    if d[2] in hex_open:
        yield 'L'
    if d[3] in hex_open:
        yield 'R'

def search(x, y, code, path=''):
    if x == 3 and y == 3:
        yield path
        return
    for door in open_doors(code, path):
        if door == 'U' and y > 0:
            yield from search(x, y-1, code, path+door)
        elif door == 'D' and y < 3:
            yield from search(x, y+1, code, path+door)
        elif door == 'L' and x > 0:
            yield from search(x-1, y, code, path+door)
        elif door == 'R' and x < 3:
            yield from search(x+1, y, code, path+door)

code = 'ioramepc'
paths = list(search(0, 0, code))
print(len(paths))
print(min(paths, key=len))
print(len(max(paths, key=len)))
