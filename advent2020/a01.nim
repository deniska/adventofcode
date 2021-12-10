from os import commandLineParams
from strutils import parseInt, split, strip
from sequtils import map
from sugar import `=>`

let nums = readFile(commandLineParams()[0])
            .strip
            .split
            .map(s => strip(s))
            .map(parseInt)

block part1:
  for i in nums:
    for j in nums:
      if i + j == 2020:
        echo i * j
        break part1

block part2:
  for i in nums:
    for j in nums:
      for k in nums:
        if i + j + k == 2020:
          echo i * j * k
          break part2
