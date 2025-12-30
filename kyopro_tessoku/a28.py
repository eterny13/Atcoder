N = int(input())

ans = []
v = 0
for _ in range(N):
  t, a = list(input().split())

  a = int(a)
  if t == '+':
    v += a 
  elif t == '-':
    v -= a 
  elif t == '*':
    v *= a 
  
  if v < 0:
    v += 10000
  v %= 10000 
  print(v)
