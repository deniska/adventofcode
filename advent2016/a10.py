import re
import attr
import fileinput
import collections

@attr.s
class Bot:
    values = attr.ib(attr.Factory(list))
    higher = attr.ib(default=None)
    lower = attr.ib(default=None)

@attr.s
class Output:
    values = attr.ib(attr.Factory(list))

id_to_bot = collections.defaultdict(Bot)
id_to_output = collections.defaultdict(Output)
things = {'output': id_to_output, 'bot': id_to_bot}
for line in fileinput.input():
    line = line.strip()
    m = re.match(r'value (\d+) goes to bot (\d+)', line)
    if m:
        value = int(m.group(1))
        bot_id = int(m.group(2))
        bot = id_to_bot[bot_id]
        bot.values.append(value)
        continue
    m = re.match(r'bot (\d+) gives low to (output|bot) (\d+)'
            ' and high to (output|bot) (\d+)', line)
    if m:
        bot_id = int(m.group(1))
        bot = id_to_bot[bot_id]
        bot.lower = things[m.group(2)][int(m.group(3))]
        bot.higher = things[m.group(4)][int(m.group(5))]

while True:
    for id, bot in id_to_bot.items():
        if len(bot.values) == 2:
            break
    else:
        break
    low, high = sorted(bot.values)
    if low == 17 and high == 61:
        print(id)
    bot.values.clear()
    bot.higher.values.append(high)
    bot.lower.values.append(low)

prod = 1
for i in 0, 1, 2:
    for value in id_to_output[i].values:
        print(value)
        prod *= value

print(prod)
