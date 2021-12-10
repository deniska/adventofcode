state = 'A'
diag = 12459852
tape = [0] * 1_000_000
cur = len(tape) // 2

states = {
        'A': [(1, 1, 'B'), (1, -1, 'E')],
        'B': [(1, 1, 'C'), (1, 1, 'F')],
        'C': [(1, -1, 'D'), (0, 1, 'B')],
        'D': [(1, 1, 'E'), (0, -1, 'C')],
        'E': [(1, -1, 'A'), (0, 1, 'D')],
        'F': [(1, 1, 'A'), (1, 1, 'C')]
        }

for _ in range(diag):
    tape[cur], d, state = states[state][tape[cur]]
    cur += d

print(tape.count(1))
