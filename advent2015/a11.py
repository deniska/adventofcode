pw = bytearray(b'hepxcrrq')

def inc():
    r = len(pw) - 1
    while True:
        pw[r] += 1
        if pw[r] > 122:
            pw[r] = 97
            r -= 1
        else:
            break

def check(pw):
    for c in pw:
        if c in {105, 108, 111}:
            return False
    for i in range(2, len(pw)):
        if pw[i] - pw[i-1] == 1 and pw[i-1] - pw[i-2] == 1:
            break
    else:
        return False

    i = 0
    c = 0
    while i < len(pw) - 1:
        if pw[i] == pw[i+1]:
            c += 1
            i += 2
        else:
            i += 1
    if c < 2:
        return False
    return True

for _ in range(2):
    while True:
        inc()
        if check(pw):
            print(pw.decode('ascii'))
            break
