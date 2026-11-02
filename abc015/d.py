
W = int(input())
N, K = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W+1) for _ in range(K+1)]

for i in range(1, N+1):
  a,b = AB[i-1]
  for j in range(K, 0, -1):
    for l in range(W, 0, -1):
      if l >= a:
        dp[j][l] = max(dp[j][l], dp[j-1][l-a]+b)

print(dp[K][W])
