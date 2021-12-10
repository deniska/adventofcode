import sys
import networkx as nx

bags = nx.DiGraph()

with open(sys.argv[1]) as f:
    for line in f:
        words = line.split()
        color1 = ' '.join(words[:2])
        if words[4] == 'no':
            continue
        idx = 4
        colors = []
        counts = []
        while idx < len(words):
            colors.append(' '.join(words[idx+1:idx+3]))
            counts.append(int(words[idx]))
            idx += 4
        for count, color in zip(counts, colors):
            bags.add_edge(color1, color, count=count)

def part2(bags, bag):
    s = 0
    for u, v, data in bags.out_edges(bag, True):
        count = data['count']
        s += data['count'] + data['count'] * part2(bags, v)
    return s

SANTA_BAG = 'shiny gold'

print(len(nx.algorithms.dag.ancestors(bags, SANTA_BAG)))
print(part2(bags, SANTA_BAG))
