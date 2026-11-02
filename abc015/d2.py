W = int(input())
N, K = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[[-1] * (W+1) for _ in range(K+1)] for _ in range(N+1)]

dp[0][0][0] = 0

for i in range(1, N+1):
  a,b = AB[i-1]

  for j in range(K+1):
    for l in range(W+1):
      if dp[i - 1][j][l] != -1:
          dp[i][j][l] = max(dp[i][j][l], dp[i - 1][j][l])
      
      if j > 0 and l >= a and dp[i-1][j-1][l-a] != -1:
          dp[i][j][l] = max(dp[i][j][l], dp[i-1][j-1][l-a]+b)

ans = 0
for k in range(K + 1):
    for w in range(W + 1):
        if dp[N][k][w] != -1:
            ans = max(ans, dp[N][k][w])

print(ans)
