N,W = map(int, input().split())

vs = []
ws = []
INF = 0
dp = [[INF] * (W+1) for _ in range(N+1)]

for i in range(N):
  v,w = map(int, input().split())
  vs.append(v)
  ws.append(w)


dp[0][0] = 0
for i in range(1, N+1):
  for j in range(W+1):
    if j >= ws[i-1]:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-ws[i-1]]+vs[i-1])

print(dp[N][W])
