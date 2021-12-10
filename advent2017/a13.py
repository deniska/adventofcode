import ast

with open('input13.txt') as f:
    d = ast.literal_eval('{' + f.read().replace('\n', ',') + '}')

def go(offset=0):
    s = 0
    caught = False
    for i, v in d.items():
        if (i+offset) % ((v-1)*2) == 0:
            s += i * v
            caught = True
    return caught, s
_, s = go()
print(s)

i = 0
while True:
    caught, _ = go(i)
    if not caught:
        print(i)
        break
    i += 1
