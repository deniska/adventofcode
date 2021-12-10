import sys
import re

def byr(v):
    if len(v) != 4:
        return False
    v = int(v)
    return 1920 <= v <= 2002

def iyr(v):
    if len(v) != 4:
        return False
    v = int(v)
    return 2010 <= v <= 2020

def eyr(v):
    if len(v) != 4:
        return False
    v = int(v)
    return 2020 <= v <= 2030

def hgt(v):
    m = re.match(r'(\d+)(cm|in)$', v)
    if not m:
        return False
    n, u = m.groups()
    n = int(n)
    if u == 'cm':
        return 150 <= n <= 193
    elif u == 'in':
        return 59 <= n <= 76

def hcl(v):
    return re.match(r'#[0-9a-f]{6}$', v) is not None

def ecl(v):
    return v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

def pid(v):
    return re.match(r'\d{9}$', v) is not None

def cid(v):
    return True

fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    #'cid',
    }

cnt = 0
cnt1 = 0
lines = []
with open(sys.argv[1]) as f:
    for line in f:
        lines.append(line.strip())
lines.append('')

current_passport = set()
valid = True
for line in lines:
    if line == '':
        if current_passport >= fields:
            cnt += 1
            if valid:
                cnt1 += 1
        current_passport = set()
        valid = True
        continue
    for kv in line.split():
        k, v = kv.split(':')
        current_passport.add(k)
        if not globals()[k](v):
            valid = False

print(cnt)
print(cnt1)
