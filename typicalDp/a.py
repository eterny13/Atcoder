N = int(input())

P = list(map(int, input().split()))

sp = sum(P)
dp = [[False] * (sp+1) for _ in range(N+1)]

dp[0][0] = True
for i in range(1,N+1):
  for j in range(sp+1):
    dp[i][j] = dp[i-1][j]
  for j in range(sp, P[i-1]-1, -1):
    if dp[i][j-P[i-1]] is True:
      dp[i][j] = True 

print(sum(dp[N]))
