import sys
import math
import operator

with open(sys.argv[1]) as f:
    hexbits = f.read().strip()

binbits = ''.join(f'{int(i, 16):>04b}' for i in hexbits)

vsum = 0

ops = {
        0: 'sum',
        1: 'prod',
        2: 'min',
        3: 'max',
        5: 'gt',
        6: 'lt',
        7: 'eq',
        }

def parse(packet):
    global vsum
    version = int(packet[:3], 2)
    vsum += version
    ptype = int(packet[3:6], 2)
    if ptype == 4: # literal
        i = 6
        ns = ''
        while True:
            p = packet[i:i+5]
            ns += p[1:]
            i += 5
            if p[0] == '0':
                break
        n = int(ns, 2)
        return packet[i:], str(n)
    else: # operator
        ltype = packet[6]
        parts = [ops[ptype], '(']
        if ltype == '0':
            total_bits = int(packet[7:7+15], 2)
            rest = packet[7+15:7+15+total_bits]
            params = []
            while rest:
                rest, p = parse(rest)
                params.append(p)
            parts.append(', '.join(params))
            parts.append(')')
            return packet[7+15+total_bits:], ''.join(parts)
        else:
            total_packets = int(packet[7:7+11], 2)
            rest = packet[7+11:]
            params = []
            for i in range(total_packets):
                rest, p = parse(rest)
                params.append(p)
            parts.append(', '.join(params))
            parts.append(')')
            return rest, ''.join(parts)


_, f = parse(binbits)
print(vsum)
part2 = int(eval(f, {
    'prod': lambda *x: math.prod(x),
    'sum': lambda *x: sum(x),
    'min': lambda *x: min(x),
    'max': lambda *x: max(x),
    'gt': operator.gt,
    'lt': operator.lt,
    'eq': operator.eq,
    }))
print(part2)
