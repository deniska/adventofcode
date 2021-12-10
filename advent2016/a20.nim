import strutils

const M = 4294967295

var
  filters: seq[tuple[a: int, b: int]] = @[]
  range_s: seq[string]
  range_from, range_to: int

var f = open("input20")

for line in f.lines:
  range_s = line.split('-')
  range_from = range_s[0].parseInt()
  range_to = range_s[1].parseInt()
  filters.add((range_from, range_to))

f.close()

var c = 0

for i in 0..M:
  var found = false
  for f in filters:
    if i >= f.a and i <= f.b:
      found = true
      break
  if not found:
    c += 1

echo c
