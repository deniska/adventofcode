import re
import sys
from PIL import Image

robots = []
with open(sys.argv[1]) as f:
    for line in f:
        robots.append([int(x) for x in re.findall(r'[-0-9]+', line)])

w = 101
h = 103
#w = 11
#h = 7
hw = w // 2
hh = h // 2

steps = 100
q0 = q1 = q2 = q3 = 0
for x, y, dx, dy in robots:
    nx = (x + dx * steps) % w
    ny = (y + dy * steps) % h
    if nx < hw and ny < hh:
        q0 += 1
    elif nx > hw and ny < hh:
        q1 += 1
    elif nx > hw and ny > hh:
        q2 += 1
    elif nx < hw and ny > hh:
        q3 += 1
print(q0*q1*q2*q3)

def save_image(steps, robots):
    img = Image.new('1', (w, h))
    for x, y in robots:
        img.putpixel((x, y), 255)
    img.save(f'img14/{steps:04d}.png')

for steps in range(77, 10000, 101):
    nrobots = []
    for i, (x, y, dx, dy) in enumerate(robots):
        nx = (x + dx * steps) % w
        ny = (y + dy * steps) % h
        nrobots.append((nx, ny))
    save_image(steps, nrobots)
    # 77 (121) 178 (224) 279 (327) 380 ("interesting" images are 101 pixels apart starting from 77)
