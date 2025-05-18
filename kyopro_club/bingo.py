N, M, S = map(int, input().split())
MOD = 100000

dp = [[0] * (S+1) for _ in range(N*N+1)]

dp[0][0] = 1
for i in range(1, M+1):
  for j in range(N*N, -1, -1):
    for k in range(i, S+1):
        dp[j][k] += dp[j-1][k-i]
        dp[j][k] %= MOD

print(dp[N*N][S])
