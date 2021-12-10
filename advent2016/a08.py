from PIL import Image, ImageDraw
import numpy as np
import fileinput
import re

np.set_printoptions(linewidth=200)

screen = np.zeros((6, 50), dtype=np.int)

def nums(line):
    nums = [int(m) for m in re.findall('\d+', line)]
    return nums

i = 0
rect_size = 20
padding = 2
def save(screen):
    return
    global i
    img = Image.new('RGB',
            ((rect_size+padding*2) * 50, (rect_size+padding*2) * 6)
            )
    draw = ImageDraw.Draw(img)
    for (y, x), v in np.ndenumerate(screen):
        if not v:
            continue
        draw.rectangle([
            x * (rect_size+padding*2) + padding,
            y * (rect_size+padding*2) + padding,
            x * (rect_size+padding*2) + padding + rect_size,
            y * (rect_size+padding*2) + padding + rect_size,
            ], fill = (0, 204, 0))
    fname = 'img8/{:05}.png'.format(i)
    img.save(fname)
    print('Saved {}'.format(fname))
    i += 1


for line in fileinput.input():
    line = line.strip()
    print(line)
    if line.startswith('rect'):
        w, h = nums(line)
        screen[:h, :w] = 1
    elif line.startswith('rotate row y'):
        y, by = nums(line)
        row = screen[y, :]
        for _ in range(by):
            row = np.roll(row, by//abs(by))
            screen[y, :] = row
            save(screen)
    elif line.startswith('rotate column x'):
        x, by = nums(line)
        col = screen[:, x]
        for _ in range(by):
            col = np.roll(col, by//abs(by))
            screen[:, x] = col
            save(screen)
    for _ in range(5):
        save(screen)
    #print(screen)

for _ in range(30):
    save(screen)
print(screen)
print(np.sum(screen))
