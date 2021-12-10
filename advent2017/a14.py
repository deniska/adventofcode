import networkx as nx
from a10 import hash2

g = nx.Graph()
inp = 'hfdlxzhv'
s = 0
prev = None
for i in range(128):
    b = bin(int(hash2(f'{inp}-{i}'), 16))[2:].rjust(128, '0')
    for j in range(128):
        if b[j] == '1':
            g.add_node((i, j))
        if j < 127 and b[j] == '1' and b[j+1] == '1':
            g.add_edge((i, j), (i, j+1))
        if prev and prev[j] == '1' and b[j] == '1':
            g.add_edge((i-1, j), (i, j))
    s += b.count('1')
    prev = b
print(s)
print(nx.number_connected_components(g))
