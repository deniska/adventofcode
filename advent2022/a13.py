import sys
import json
import functools

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip().split('\n\n')
    s = 0
    packets = []
    for idx, pair in enumerate(data, start=1):
        a, b = pair.split('\n')
        a = json.loads(a)
        b = json.loads(b)
        packets.append(a)
        packets.append(b)
        if check_order(a, b):
            s += idx
    print(s)
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=functools.cmp_to_key(check_order_cmp), reverse=True)
    print((packets.index([[2]])+1) * (packets.index([[6]])+1))


def check_order(a, b):
    if isinstance(a, list) and isinstance(b, int):
        b = [b]

    if isinstance(a, int) and isinstance(b, list):
        a = [a]

    idx = 0
    while True:
        if idx >= len(a) and idx >= len(b):
            return None
        if idx >= len(a):
            return True
        if idx >= len(b):
            return False
        left = a[idx]
        right = b[idx]
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            if left > right:
                return False
        else:
            res = check_order(left, right)
            if res is not None:
                return res
        idx += 1

def check_order_cmp(a, b):
    if check_order(a, b):
        return 1
    return -1

if __name__ == '__main__':
    main()
