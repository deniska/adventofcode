import re
from string import ascii_lowercase as alphabet
from collections import Counter

length = len(alphabet)
def shift(s, shift):
    shift = shift % length
    translation = str.maketrans(alphabet, alphabet[shift:] + alphabet[:shift])
    return s.translate(translation)

id_sum = 0
with open('input4.txt') as f:
    for line in f:
        m = re.match(r'([a-z-]+)(\d+)\[([a-z]+)\]', line)
        name = m.group(1).strip('-')
        counter = Counter(name.replace('-', ''))
        id = int(m.group(2))
        checksum = m.group(3)
        my_checksum = ''.join(x[0] for x in
                sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))[:5])
        if checksum == my_checksum:
            id_sum += id
            print(name, id, shift(name, id))
print(id_sum)
