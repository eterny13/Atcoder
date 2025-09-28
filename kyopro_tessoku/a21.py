N = int(input())
P = []
A = []
P.append(None)
A.append(None)
for i in range(N):
  p,a = map(int, input().split())
  P.append(p)
  A.append(a)

dp = [[None for _ in range(N+1)] for _ in range(N+1)]

dp[1][N] = 0

for i in range(N-2, -1, -1):
  for l in range(1, N-i+1):
    r = l + i

    score1 = 0
    if l >= 2 and l <= P[l-1] and P[l-1] <= r:
      score1 = A[l-1]
    
    score2 = 0
    if r <= N-1 and l <= P[r+1] and P[r+1] <= r:
      score2 = A[r+1]
    
    if l == 1:
      dp[l][r] = dp[l][r+1]+score2
    elif r == N:
      dp[l][r] = dp[l-1][r]+score1
    else:
      dp[l][r] = max(dp[l-1][r]+score1, dp[l][r+1]+score2) 

ans = 0
for i in range(1, N+1):
  ans = max(ans, dp[i][i])

print(ans)
