N = int(input())
hs = list(map(int, input().split()))

dp = [0 for i in range(N+1)]

dp[2] = abs(hs[1]-hs[0])
for i in range(3, N+1):
  dp[i] = min(abs(hs[i-1]-hs[i-2]) + dp[i-1], abs(hs[i-1]-hs[i-3]) + dp[i-2])

print(dp[N])
