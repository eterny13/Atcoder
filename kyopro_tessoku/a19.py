N,S = map(int, input().split())

ks = []
for i in range(N):
  w,v = map(int, input().split())
  ks.append([w,v])

dp = [[0 for _ in range(S+1)] for _ in range(N+1)]

for i in range(1, N+1):
  w = ks[i-1][0]
  v = ks[i-1][1]
  for j in range(S+1):
    dp[i][j] = dp[i-1][j]
    if j >= w:
      dp[i][j] = max(v + dp[i-1][j-w], dp[i][j])

print(dp[N][S])
