import re
import sys

instructions = []

with open(sys.argv[1]) as f:
    for line in f:
        state = line.partition(' ')[0]
        coords = [int(a) for a in re.findall(r'-?\d+', line)]
        instructions.append((state == 'on', coords))

code = []
code.append('#include <iostream>')
code.append('')
code.append('bool calc_point(int x, int y, int z) {')
for s, (x1, x2, y1, y2, z1, z2) in reversed(instructions):
    code.append(f' if (({x1} <= x) && (x <= {x2})'
            f' && ({y1} <= y) && (y <= {y2})'
            f' && ({z1} <= z) && (z <= {z2}))')
    code.append(f'  return {str(s).lower()};')
code.append(' return false;')
code.append('}\n')

x_splits = set()
y_splits = set()
z_splits = set()
for s, (x1, x2, y1, y2, z1, z2) in instructions:
    x_splits.add(x1)
    x_splits.add(x2+1)
    y_splits.add(y1)
    y_splits.add(y2+1)
    z_splits.add(z1)
    z_splits.add(z2+1)
x_splits = sorted(x_splits)
y_splits = sorted(y_splits)
z_splits = sorted(z_splits)

def s(a):
    return ', '.join(str(i) for i in a)

code.append(f'const int x_splits[]{{{s(x_splits)}}};')
code.append(f'const int y_splits[]{{{s(y_splits)}}};')
code.append(f'const int z_splits[]{{{s(z_splits)}}};')
code.append('')
code.append(f'const int x_len = {len(x_splits)};')
code.append(f'const int y_len = {len(y_splits)};')
code.append(f'const int z_len = {len(z_splits)};')

code.append(r'''
int main(int argc, char** argv) {
    long long vol = 0;
    for (int ix = 0; ix < x_len-1; ix++) {
        for (int iy = 0; iy < y_len-1; iy++) {
            for (int iz = 0; iz < z_len-1; iz++) {
                int sx1 = x_splits[ix];
                int sx2 = x_splits[ix + 1];
                int sy1 = y_splits[iy];
                int sy2 = y_splits[iy + 1];
                int sz1 = z_splits[iz];
                int sz2 = z_splits[iz + 1];
                if (calc_point(sx1, sy1, sz1)) {
                    vol += ((long long) sx2 - sx1) * (sy2 - sy1) * (sz2 - sz1);
                }
            }
        }
    }
    std::cout << vol << "\n";
}
''')

with open('a22_gen.cpp', 'w') as f:
    f.write('\n'.join(code))
