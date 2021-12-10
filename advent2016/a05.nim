{.experimental.}
import threadpool
import strutils
import md5

var
  password: string = "________"
  i: int = 0
  c: int = 0

const
  door_code = "cxdnnyjw"

type pos_char = tuple[position: int, character: char]
proc find_digits(start: int, finish: int): seq[pos_char] =
  var
    saved_context: MD5Context
    context: MD5Context
    digest: MD5Digest
  saved_context.md5Init()
  saved_context.md5Update(door_code.cstring, door_code.len)
  result = @[]
  for i in start..finish - 1:
    context = saved_context
    let s = $i
    context.md5Update(s.cstring, s.len)
    context.md5Final(digest)
    if digest[0] == 0 and digest[1] == 0 and digest[2] < 8:
      let
        digit = digest[2].int
        character = ($digest)[6]
      result.add((position: digit, character: character))

let
  thread_count = 4
  chunk_per_thread = 100000
while true:
  var chunks: seq[FlowVar[seq[pos_char]]] = @[]
  for k in 0..thread_count-1:
    chunks.add(spawn find_digits(i+k*chunk_per_thread, i+(k+1)*chunk_per_thread))
  for chunk in chunks:
    for digit in ^chunk:
      if password[digit.position] == '_':
        password[digit.position] = digit.character
        echo password
        c += 1
  if c == 8:
    break
  i += thread_count * chunk_per_thread

echo password
