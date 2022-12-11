import sys
import math

class Monkey:
    def __init__(self, items, op, div_test, if_true, if_false):
        self.items = items
        self.op = op
        self.div_test = div_test
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_count = 0
        self.worry_mod = 0

    def round(self):
        ret_true = []
        ret_false = []
        for item in self.items:
            self.inspect_count += 1
            item = self.op(item)
            item %= self.worry_mod
            if item % self.div_test == 0:
                ret_true.append(item)
            else:
                ret_false.append(item)
        self.items.clear()
        return {self.if_true: ret_true, self.if_false: ret_false}


with open(sys.argv[1]) as f:
    data = f.read()

monkeys_s = data.split('\n\n')
monkeys = []
for m in monkeys_s:
    lines = m.split('\n')
    items = [int(a) for a in lines[1].partition(': ')[2].split(', ')]
    op = eval(f'lambda old: {lines[2].partition("= ")[2]}')
    div_test = int(lines[3].split()[-1])
    if_true = int(lines[4].split()[-1])
    if_false = int(lines[5].split()[-1])
    monkeys.append(Monkey(items, op, div_test, if_true, if_false))

worry_mod = math.lcm(*(m.div_test for m in monkeys))
for m in monkeys:
    m.worry_mod = worry_mod

for i in range(10000):
    for m in monkeys:
        res = m.round()
        for k, v in res.items():
            monkeys[k].items += v

mbiz = sorted((m.inspect_count for m in monkeys), reverse=True)
print(mbiz[0] * mbiz[1])
