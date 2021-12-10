from threading import Thread
from itertools import permutations
from intcode_q import run
from queue import Queue
import sys

def main():
    with open(sys.argv[1]) as f:
        prog = f.read().strip().split(',')
    prog = [int(p) for p in prog]
    max_p = 0
    max_phases = None
    for phases in permutations(range(5, 10)):
        amps = []
        queues = [Queue() for _ in range(5)]
        for i, phase in enumerate(phases):
            amp = Thread(target=run,
                    args=(prog, queues[i], queues[(i+1)%5]))
            amp.start()
            amps.append(amp)
            queues[i].put(phase)
        queues[0].put(0)
        for amp in amps:
            amp.join()
        p = queues[0].get()
        if p > max_p:
            max_p = p
            max_phases = phases
    print(max_phases)
    print(max_p)

if __name__ == '__main__':
    main()
