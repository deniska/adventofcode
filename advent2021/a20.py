import sys

image = set()

with open(sys.argv[1]) as f:
    image_enhancement_algorithm_string = next(f).strip()
    next(f)
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c == '#':
                image.add((x, y))

def neighbours(p):
    x, y = p
    for j in range(-1, 2):
        for i in range(-1, 2):
            yield x + i, y + j

def bounds(image):
    max_x = max(a[0] for a in image)
    max_y = max(a[1] for a in image)
    min_x = min(a[0] for a in image)
    min_y = min(a[1] for a in image)
    return min_x, max_x, min_y, max_y

def iter_pixels(image):
    min_x, max_x, min_y, max_y = bounds(image)
    for y in range(min_y-1, max_y+2):
        for x in range(min_x-1, max_x+2):
            yield (x, y)

def enhance(image, gen):
    min_x, max_x, min_y, max_y = bounds(image)
    new_image = set()
    for p in iter_pixels(image):
        idx = 0
        for n in neighbours(p):
            idx <<= 1
            if n in image:
                idx |= 1
            x, y = n
            if x < min_x or y < min_y or x > max_x or y > max_y:
                if image_enhancement_algorithm_string[0] == '#' and gen % 2 == 1:
                    idx |= 1
        if image_enhancement_algorithm_string[idx] == '#':
            new_image.add(p)
    return new_image

def part1():
    print(len(enhance(enhance(image, 0), 1)))

def part2():
    img = image
    for i in range(50):
        img = enhance(img, i)
    print(len(img))

part1()
part2()
