import sys
import itertools

reports = []

with open(sys.argv[1]) as f:
    for line in f:
        reports.append([int(a) for a in line.split()])

def is_safe(report):
    diff = report[1] - report[0]
    if diff > 0:
        increasing = True
    elif diff < 0:
        increasing = False
    else:
        return False
    for a, b in itertools.pairwise(report):
        diff = b - a
        if increasing and diff not in (1, 2, 3):
            return False
        elif not increasing and diff not in (-1, -2, -3):
            return False
    return True

cnt = 0
for report in reports:
    if is_safe(report):
        cnt += 1
print(cnt)

cnt = 0
for report in reports:
    if is_safe(report):
        cnt += 1
    else:
        for i in range(0, len(report)):
            report1 = report.copy()
            del report1[i]
            if is_safe(report1):
                cnt += 1
                break
print(cnt)
