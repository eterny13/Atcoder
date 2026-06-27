N = int(input())

T = []
for _ in range(N):
  t = int(input())
  T.append(t)

ans = 10**18
for i in range(1<<N):
  fst = 0
  snd = 0
  for j in range(N):
    if (i>>j) & 1:
      fst += T[j]
    else:
      snd += T[j]
  
  p = max(fst, snd)
  ans = min(ans, p)

print(ans)
