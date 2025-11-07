N = int(input())
S = input()

dp = [[None] * N for _ in range(N)]

for i in range(N):
  dp[i][i] = 1

for i in range(N-1):
  if S[i] == S[i+1]:
    dp[i][i+1] = 2
  else:
    dp[i][i+1] = 1

for l in range(2, N):
  for i in range(0, N-l):
    r = l + i
    if S[i] == S[r]:
      dp[i][r] = max(dp[i+1][r], dp[i][r-1], dp[i+1][r-1]+2)
    else:
      dp[i][r] = max(dp[i][r-1], dp[i+1][r])

print(dp[0][N-1])
