D, G = list(map(int, input().split()))

pc = []

for i in range(D):
  pt = (i+1) * 100
  p,c = list(map(int, input().split()))
  pc.append([p,c, pt])

pc.reverse()


ans = float('inf')
ansv = []
for i in range(1<<D):
  g = G
  for j in range(D):
    if (i>>j) & 1:
      p,c,pt = pc[j]

      t= pt * p + c
      if t < g:
        g -= t
        if ans == None: 
          ans = p
        else:
          ans += p
      else:
        while (t - c - pt >= g):
          t -= pt
          p -= 1
        
        if ans == None: 
          ans = p
          g = 0
        else:
          ans += p
          g = 0
  if g <= 0:
    ansv.append(ans)
  ans = None

print(min(ansv))
