import strutils
import md5

var
  saved_context: MD5Context
  context: MD5Context
  digest: MD5Digest
  password: string = "________"
  i: int = 0
  c: int = 0
  digit: int

const
  door_code = "cxdnnyjw"

saved_context.md5Init()
saved_context.md5Update(door_code.cstring, door_code.len)

while true:
  context = saved_context
  var s = $i
  context.md5Update(s.cstring, s.len)
  context.md5Final(digest)
  if digest[0] == 0 and digest[1] == 0 and digest[2] < 8:
    digit = digest[2].int
    if password[digit] == '_':
      password[digit] = ($digest)[6]
      echo password
      c += 1
      if c == 8:
        break
  i += 1

echo password
