N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N):
  if i == 1:
    dp[i+1] = dp[i]+A[i-1]
    continue
  dp[i+1] = min(dp[i]+A[i-1], dp[i-1]+B[i-2])

print(dp[N])
