a,b = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(b)]

INF = 10**18
dp = [INF] * (1<<a)
dp[0] = 0

for row in A:
  row_mask = 0
  for k, v in enumerate(row):
    if v == 1:
      row_mask |= (1<<k)
  
  next_dp = [INF] * (1<<a)
  for now in range(1<<a):
    if dp[now] < next_dp[now]:
      next_dp[now] = dp[now]
    
    new_mask = now | row_mask
    if dp[now] + 1 < next_dp[new_mask]:
      next_dp[new_mask] = dp[now] + 1
  dp = next_dp

ans = dp[(1<<a)-1]
print(ans if ans < INF else -1)
