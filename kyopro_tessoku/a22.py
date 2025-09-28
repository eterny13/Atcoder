N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [-1000000000] * (N+1)
dp[1] = 0
for i in range(1, N):
  dp[A[i-1]] = max(dp[A[i-1]], dp[i] + 100)
  dp[B[i-1]] = max(dp[B[i-1]], dp[i] + 150)

print(dp[N])
