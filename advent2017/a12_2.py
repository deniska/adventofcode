import networkx as nx

with open('input12.txt') as f:
    s = f.read()
nl = '\n'
d = eval(f'{{{s.replace("<->", ":(").replace(f"{nl}", ",),")}}}')
g = nx.convert.from_dict_of_lists(d)

print(len(nx.node_connected_component(g, 0)))
print(nx.number_connected_components(g))
