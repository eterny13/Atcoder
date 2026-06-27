s = input()

n = len(s)

st = ""
for i in range(1<<(n-1)):
  cur = int(s[0])
  st = s[0]
  for j in range(n-1):
    if (i >> j) & 1:
      cur -= int(s[j+1])
      st += "-" + s[j+1]
    else:
      cur += int(s[j+1])
      st += "+" + s[j+1]

  st += "=" + str(cur)
  #print(st)
  if cur == 7:
    break

print(st)
