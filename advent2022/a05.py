import sys

stacks1 = []
stacks2 = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip('\n')
        if not line:
            break
        if not stacks1:
            stack_cnt = (len(line) + 1) // 4
            for i in range(stack_cnt):
                stacks1.append([])
                stacks2.append([])
        for stack_n, i in enumerate(range(1, len(line), 4)):
            c = line[i]
            if c == ' ':
                continue
            if c == '1':
                break
            stacks1[stack_n].insert(0, c)
            stacks2[stack_n].insert(0, c)
        
    for line in f:
        parts = line.split()
        cnt = int(parts[1])
        stack_from = int(parts[3]) - 1
        stack_to = int(parts[5]) - 1
        stacks2[stack_to] += stacks2[stack_from][-cnt:]
        for i in range(cnt):
            stacks1[stack_to].append(stacks1[stack_from].pop())
            stacks2[stack_from].pop()


print(''.join(s[-1] for s in stacks1))
print(''.join(s[-1] for s in stacks2))
