components = []

with open('input24.txt') as f:
    for line in f:
        a, b = line.split('/')
        a = int(a)
        b = int(b)
        components.append((a, b))

longest_len = 0
longest_strength = 0
def bridge(free_port=0, components_left=None, acc=0, brlen=0):
    global longest_len, longest_strength
    if components_left is None:
        components_left = components
    m = []
    for comp in components_left:
        if free_port == comp[0]:
            c = list(components_left)
            c.remove(comp)
            m.append(bridge(comp[1], c, acc + comp[0] + comp[1], brlen + 1))
        elif free_port == comp[1]:
            c = list(components_left)
            c.remove(comp)
            m.append(bridge(comp[0], c, acc + comp[0] + comp[1], brlen + 1))
    if m:
        return max(m)
    if brlen >= longest_len:
        longest_len = brlen
        if acc > longest_strength:
            longest_strength = acc
    return acc

print(bridge())
print(longest_strength)
