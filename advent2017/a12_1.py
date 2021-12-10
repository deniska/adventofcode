import networkx as nx

g = nx.Graph()
with open('input12.txt') as f:
    for line in f:
        confrom, _, *conto = line.split()
        confrom = int(confrom)
        conto = [int(c.strip(',')) for c in conto]
        for c in conto:
            g.add_edge(confrom, c)

print(len(nx.node_connected_component(g, 0)))
print(nx.number_connected_components(g))
