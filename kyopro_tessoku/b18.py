n,s = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0 for _ in range(s+1)] for _ in range(n+1)]

dp[0][0] = 1
for i in range(1, n+1):
  for j in range(s+1):
    dp[i][j] = dp[i-1][j]
    if j >= A[i-1]:
      dp[i][j] += dp[i-1][j-A[i-1]]

if dp[n][s] > 0:
  route = []
  j = s
  for i in range(n,0,-1):
    if dp[i-1][j] == 0:
      route.append(i)
      j -= A[i-1]

  route.reverse()
  print(len(route))
  print(*route)
else:
  print(-1)
