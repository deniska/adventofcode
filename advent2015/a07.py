import sys

def q(v):
    if v.isdigit():
        return v
    return f'(_{v}() & 0xffff)'

ops = {'AND': '&', 'OR': '|', 'LSHIFT': '<<', 'RSHIFT': '>>'}

prog = ['import functools']
with open(sys.argv[1]) as f:
    for line in f:
        parts = line.strip().split()
        prog.append('@functools.cache')
        if len(parts) == 3:
            src, _, dst = parts
            src = q(src)
            prog.append(f'def _{dst}(): return {src}')
        elif len(parts) == 4:
            _, src, _, dst = parts
            src = q(src)
            prog.append(f'def _{dst}(): return ~{src}')
        else:
            src1, op, src2, _, dst = parts
            src1 = q(src1)
            src2 = q(src2)
            op = ops[op]
            prog.append(f'def _{dst}(): return {src1} {op} {src2}')

d = {}
exec('\n'.join(prog), d)
result1 = d['_a']() & 0xffff
print(result1)
prog.append(f'def _b(): return {result1}')
exec('\n'.join(prog), d)
result2 = d['_a']() & 0xffff
print(result2)
