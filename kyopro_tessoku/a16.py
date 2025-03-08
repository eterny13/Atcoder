n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0 for _ in range(n+2)]

for i in range(1, n):
  if i == 1:
    dp[i] = dp[i-1] + A[i-1]
    continue
  dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])

print(dp[n-1])
