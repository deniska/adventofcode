disks = [13, 5, 17, 3, 7, 19, 11]
initpos = [11, 0, 11, 0, 2, 17, 0]

def trial(time):
    for i, v in enumerate(initpos):
        q = (v + time + i + 1) % disks[i]
        if q != 0:
            break
    else:
        print(time)
        return True
    return False

t = 0
while not trial(t):
    t += 1
