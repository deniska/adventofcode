from collections import defaultdict
import threading
import queue


result = 0
def run(pid, inbox, outbox):
    global result
    prog = []
    with open('input18.txt') as f:
        for line in f:
            prog.append(line.strip().split())

    mem = defaultdict(int)
    mem['p'] = pid
    def get(val):
        try:
            return int(val)
        except ValueError:
            return mem[val]

    cur = 0
    i = 0
    while cur < len(prog):
        inst, *ops = prog[cur]
        if inst == 'snd':
            outbox.put(get(ops[0]))
            if pid == 1:
                result += 1
        elif inst == 'set':
            mem[ops[0]] = get(ops[1])
        elif inst == 'add':
            mem[ops[0]] = mem[ops[0]] + get(ops[1])
        elif inst == 'mul':
            mem[ops[0]] = mem[ops[0]] * get(ops[1])
        elif inst == 'mod':
            mem[ops[0]] = mem[ops[0]] % get(ops[1])
        elif inst == 'rcv':
            try:
                mem[ops[0]] = inbox.get(timeout=10)
            except queue.Empty:
                print('Timeout', pid)
                return
        elif inst == 'jgz':
            if get(ops[0]) > 0:
                cur += get(ops[1])
                continue
        else:
            raise ValueError
        cur += 1
    print('Finished', pid)

q1 = queue.Queue()
q2 = queue.Queue()

t1 = threading.Thread(target=run, args=(0, q1, q2))
t2 = threading.Thread(target=run, args=(1, q2, q1))
t1.start()
t2.start()
t1.join()
t2.join()
print(result)
