import fileinput
import re

def tls(line):
    abbas = [x for x in re.findall(r'(.)(.)\2\1', line) if x[0] != x[1]]
    hypernets = ''.join(re.findall(r'\[[^\]]+\]', line))
    if abbas:
        for abba_m in abbas:
            abba = '{0}{1}{1}{0}'.format(abba_m[0], abba_m[1])
            if abba in hypernets:
                break
        else:
            return True
    return False

def ssl(line):
    nonets = re.split(r'\[[^\]]+\]', line)
    abas = []
    for nonet in nonets:
        abas += [x for x in re.findall(r'(?=(.)(.)\1)', nonet) if x[0] != x[1]]
    hypernets = ''.join(re.findall(r'\[[^\]]+\]', line))
    if abas:
        for aba_m in abas:
            bab = '{1}{0}{1}'.format(aba_m[0], aba_m[1])
            if bab in hypernets:
                return True
    return False

assert ssl('aba[bab]xyz')
assert not ssl('xyx[xyx]xyx')
assert ssl('aaa[kek]eke')
assert ssl('zazbz[bzb]cdb')


t = 0
s = 0
for line in fileinput.input():
    line = line.strip()
    t += tls(line)
    s += ssl(line)
print(t, s)
