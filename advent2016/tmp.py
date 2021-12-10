import re
import attr
import itertools
from pprint import pprint

with open('input9.txt') as f:
    data = f.read().replace('\n', '')
regex = re.compile(r'\((\d+)x(\d+)\)')

def decompress(data):
    output = []
    cursor = 0

    while True:
        m = regex.search(data, cursor)
        if m:
            output.append(data[cursor:m.start(0)]) # data before marker
            length = int(m.group(1))
            times = int(m.group(2))
            for _ in range(times):
                output.append(data[m.end(0):m.end(0)+length])
            cursor = m.end(0) + length
        else:
            output.append(data[cursor:])
            break
    return ''.join(output)

@attr.s
class Marker:
    start = attr.ib()
    end = attr.ib()
    length = attr.ib()
    count = attr.ib()
    multiplier = attr.ib()

def mul(s):
    m = 1
    for i in s:
        m *= i
    return m

def length2(data):
    cursor = 0
    markers = []
    while True:
        m = regex.search(data, cursor)
        if m is None:
            break
        markers.append(Marker(
            start = m.start(0),
            end = m.end(0),
            length = int(m.group(1)),
            count = int(m.group(2)),
            multiplier = [1],
            ))
        cursor = m.end(0)
    for i, marker in enumerate(markers):
        #pprint(markers)
        multiplier = marker.count
        for marker2 in markers[i+1:]:
            if marker.end + marker.length < marker2.start + 1:
                break
            marker2.multiplier.append(multiplier)
            marker.multiplier = [0]
    markers.insert(0,
            Marker(start=0, end=0, length=0, count=0, multiplier=[1])
            )
    markers.append(Marker(
        start = len(data),
        end = len(data),
        length=0, count=0, multiplier=[1]
        ))
    length = markers[0].start
    for marker, next_marker in zip(markers, markers[1:]):
        multiplier = 1
        for m in marker.multiplier:
            multiplier *= m
        length += marker.count * marker.length * multiplier
        if marker.multiplier != [0]:
            length += next_marker.start - marker.end - marker.length
    pprint(markers)
    return length

assert length2('(3x3)XYZ') == len('XYZXYZXYZ')
assert length2('X(8x2)(3x3)ABCY') == len('XABCABCABCABCABCABCY')
assert length2('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
assert length2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445

print(len(decompress(data)))
print(length2(data))
