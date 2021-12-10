import networkx as nx
from a10 import hash2

g = nx.grid_2d_graph(128, 128)
inp = 'hfdlxzhv'
s = 0
for i in range(128):
    b = bin(int(hash2(f'{inp}-{i}'), 16))[2:].rjust(128, '0')
    for j in range(128):
        if b[j] == '0':
            g.remove_node((i, j))
    s += b.count('1')
print(s)
print(nx.number_connected_components(g))
