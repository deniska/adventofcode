import sys
import collections

limits = {'red': 12, 'green': 13, 'blue': 14}

s = 0
q = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        a, b = line.split(': ')
        game_no = int(a.split()[1])
        reveals = b.split('; ')
        invalid = False
        min_cnts = collections.defaultdict(int)
        for reveal in reveals:
            cubes = reveal.split(', ')
            for cube in cubes:
                cnt, color = cube.split()
                cnt = int(cnt)
                min_cnts[color] = max(cnt, min_cnts[color])
                if cnt > limits[color]:
                    invalid = True
        power = min_cnts['red'] * min_cnts['green'] * min_cnts['blue']
        q += power
        if not invalid:
            s += game_no

print(s)
print(q)
