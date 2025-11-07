N = int(input())

xy = [list(map(int, input().split())) for _ in range(N)]

INF = 10.0 ** 10
dp = [[INF] * N for _ in range((1<<N))]
dp[0][0] = 0

for b in range(1<<N):
  for i in range(N):
    if dp[b][i] < INF:
      for k in range(N):
        if (b // (1<<k)) % 2 == 0:
          x1=xy[i][0]
          y1=xy[i][1]
          x2=xy[k][0]
          y2=xy[k][1]
          dist = (((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2))) ** 0.5
          dp[b | (1<<k)][k] = min(dp[b | (1<<k)][k], dp[b][i]+dist)

print(dp[(1<<N)-1][0])
