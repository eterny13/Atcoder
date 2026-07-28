n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [[10**18] * (n+1) for _ in range(m+1)]

dp[0][0] = 0
for i in range(1, m+1):
  for j in range(n+1):
    if j >= coins[i-1]:
      dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1, dp[i-1][j-coins[i-1]]+1)
    else:
      dp[i][j] = dp[i-1][j]

#print(dp[2])
print(dp[m][n])
