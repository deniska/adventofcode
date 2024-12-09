import sys

with open(sys.argv[1]) as f:
    data = [int(c) for c in f.read().strip()]

disk = []

i = 0
c = 0
while i < len(data):
    disk.extend([c] * data[i])
    i += 1
    if i < len(data):
        disk.extend([None] * data[i])
    i += 1
    c += 1

i = 0
while True:
    while disk[-1] is None:
        disk.pop()
    while i < len(disk) and disk[i] is not None:
        i += 1
    if i >= len(disk):
        break
    disk[i] = disk.pop()

s = 0
for i, c in enumerate(disk):
    s += i * c
print(s)

files = []
free_spaces = []
c = 0
i = 0
diskpos = 0
while i < len(data):
    files.append((diskpos, data[i], c)) # position, size, id
    diskpos += data[i]
    c += 1
    i += 1
    if i < len(data):
        free_spaces.append((diskpos, data[i])) # position, size
        diskpos += data[i]
    i += 1

for i in range(len(files) - 1, -1, -1):
    file_pos, file_size, file_id = files[i]
    for free_idx, (free_pos, free_size) in enumerate(free_spaces):
        if free_pos > file_pos:
            break
        if free_size >= file_size:
            files[i] = (free_pos, file_size, file_id)
            if free_size > file_size:
                free_spaces[free_idx] = (free_pos + file_size, free_size - file_size)
            else:
                del free_spaces[free_idx]
            break

s = 0
for file_pos, file_size, file_id in files:
    for i in range(file_pos, file_pos + file_size):
        s += i * file_id
print(s)
