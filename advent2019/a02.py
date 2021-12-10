with open('input02.txt') as f:
    init_state = [int(c) for c in f.read().strip().split(',')]

def run(noun, verb):
    state = init_state.copy()
    state[1] = noun
    state[2] = verb

    i = 0
    while True:
        if state[i] == 99:
            break
        elif state[i] == 1:
            state[state[i+3]] = state[state[i+1]] + state[state[i+2]]
        elif state[i] == 2:
            state[state[i+3]] = state[state[i+1]] * state[state[i+2]]
        i += 4

    return state[0]

def main():
    print(run(12, 2))
    for n in range(100):
        print(f'n = {n}')
        for v in range(100):
            if run(n, v) == 19690720:
                print(n * 100 + v)
                return

if __name__ == '__main__':
    main()
