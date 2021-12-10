from collections import defaultdict

weights = {}
conns = defaultdict(list)

prognames_on_left = set()
prognames_on_right = set()
with open('input07.txt') as f:
    for line in f:
        parts = line.split()
        weights[parts[0]] = int(parts[1].strip('()'))
        prognames_on_left.add(parts[0])
        for part in parts[3:]:
            part = part.strip(',')
            prognames_on_right.add(part)
            conns[parts[0]].append(part)


start_node = list(prognames_on_left - prognames_on_right)[0]

def fix_weights(node):
    total_weights = []
    for new_node in conns[node]:
        total_weights.append(fix_weights(new_node))
    if len(set(total_weights)) > 1:
        print(list(zip(total_weights, conns[node])))
        print([(weights[n], n) for n in conns[node]])
    return sum(total_weights) + weights[node]

fix_weights(start_node)

