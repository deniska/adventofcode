s = '1321131112'

def it(s):
    char = s[0]
    cnt = 1
    res = []
    for i in range(1, len(s)):
        if s[i] == char:
            cnt += 1
        else:
            res.extend(str(cnt))
            res.append(char)
            char = s[i]
            cnt = 1
    res.extend(str(cnt))
    res.append(char)

    return res

for _ in range(40):
    s = it(s)

p1 = len(s)
print(p1)

for _ in range(10):
    s = it(s)

p2 = len(s)
print(p2)
