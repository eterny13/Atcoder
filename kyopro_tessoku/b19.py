N,S = map(int, input().split())

ks = []
vs = []
for i in range(N):
  w,v = map(int, input().split())
  ks.append([w,v])
  vs.append(v)

sumv = sum(vs)
dp = [[10**15 for _ in range(sumv+1)] for _ in range(N+1)]

dp[0][0] = 0
for i in range(1, N+1):
  w = ks[i-1][0]
  v = ks[i-1][1]
  for j in range(sumv+1):
    if j < v:
      dp[i][j] = dp[i-1][j]
    if j >= v:
      dp[i][j] = min(dp[i-1][j], w + dp[i-1][j-v])

ans = 0
for i in range(sumv+1):
  if dp[N][i] <= S:
    ans = i
print(ans)
