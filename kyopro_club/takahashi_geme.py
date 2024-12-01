def solve(n, k, a):
  acc = [0] * (n+1)
  for i in range(n):
    acc[i+1] = acc[i] + A[i]

  if sum(A) == k:
    return 1

  dp = [[10**18] * (n+1) for _ in range(n)]
  dp[0][0] = 0
  dp[0][1] = 1

  for i in range(1, n):
    for j in range(n+1):
      dp[i][j] = dp[i-1][j]
      if j > 0:
        # 1日前 dp[i-1][j-1] // acc[i]
        # dp[i-1][j-1] // acc[i] < wincount / a[i]
        wincount = dp[i-1][j-1] * a[i] // acc[i] + 1
        dp[i][j] = min(dp[i][j], dp[i-1][j-1] + wincount)
        #print(dp[i][j])

  ans = 0
  for i in range(n+1):
    if dp[n-1][i] <= k:
      ans = i
  return ans

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = solve(N, K, A)
print(ans)
