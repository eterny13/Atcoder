D, G = list(map(int, input().split()))

pc = []

for i in range(D):
  pt = (i+1) * 100
  p,c = list(map(int, input().split()))
  pc.append([p,c, pt])

pc.reverse()

ans = float('inf')

for i in range(1<<D):
  count =0
  score = 0

  for j in range(D):
    if (i >> j) & 1:
      p,c,pt = pc[j]
      score += pt * p + c
      count += p

  if score < G:
    for j in range(D):
      if not ((i>>j)&1):
        p,c,pt = pc[j]
        for _ in range(p):
          if score >= G: break
          score += pt
          count += 1

  if score >= G:
    ans = min(ans, count)
  
print(ans)
