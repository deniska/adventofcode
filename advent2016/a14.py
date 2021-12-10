import collections
import hashlib
import re

def del_old(triplets, it):
    while True:
        if triplets:
            if it - triplets[0][1] > 1000:
                triplets.popleft()
            else:
                break
        else:
            break

def rehash(digest):
    for _ in range(2016):
        digest = hashlib.md5(digest.encode('ascii')).hexdigest()
    return digest

def search():
    salt = b'jlmsuwbz'
    #salt = b'abc'
    md5salt = hashlib.md5()
    md5salt.update(salt)
    found = 0
    triplets = collections.deque()
    trre = re.compile(r'(.)\1\1')
    fivre = re.compile(r'(.)\1\1\1\1')
    it = 0
    while found < 64:
        md5 = md5salt.copy()
        md5.update(str(it).encode('ascii'))
        digest = md5.hexdigest()
        digest = rehash(digest)
        m = fivre.search(digest)
        if m:
            v = m.group(1)
            print('fvr', it)
            todel = []
            for i, triplet in enumerate(triplets):
                if v == triplet[0]:
                    found += 1
                    print(found, triplet[1])
                    todel.append(i)
            for i in reversed(todel):
                del triplets[i]
        m = trre.search(digest)
        if m:
            triplets.append((m.group(1), it))
        it += 1
        del_old(triplets, it)

search()
