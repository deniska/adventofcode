import sys
import itertools
from hashlib import md5

with open(sys.argv[1]) as f:
    data = f.read().strip()

def do_thing(data, zeros):
    for i in itertools.count():
        h = md5(f'{data}{i}'.encode('ascii')).hexdigest()
        if h.startswith(zeros):
            print(i)
            return

do_thing(data, '00000')
do_thing(data, '000000')
