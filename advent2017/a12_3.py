print(*(lambda nx, g: (
len(nx.node_connected_component(g, 0)),
nx.number_connected_components(g)))(*(lambda nx: (nx,
nx.convert.from_dict_of_lists(
eval(f'{{{open("input12.txt").read().replace("<->", ":(").replace(chr(10), ",),")}}}'))))(
__import__('networkx'))))
