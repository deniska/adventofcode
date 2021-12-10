import sys
import pathlib

nums = pathlib.Path(sys.argv[1]).read_text().strip().split(',')
nums = [int(n) for n in nums]

first_times = {}
second_times = {}
turn = 1

for n in nums:
    first_times[n] = turn
    turn += 1

prev = nums[-1]

while True:
    if prev not in second_times:
        prev = 0
        if 0 in first_times:
            second_times[0] = first_times[0]
        first_times[0] = turn
        if turn == 2020:
            print(0)
        elif turn == 30000000:
            print(0)
            break
    else:
        diff = first_times[prev] - second_times[prev]
        prev = diff
        if diff in first_times:
            second_times[diff] = first_times[diff]
        first_times[diff] = turn
        if turn == 2020:
            print(diff)
        elif turn == 30000000:
            print(diff)
            break
    turn += 1
