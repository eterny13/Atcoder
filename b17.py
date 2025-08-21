N = int(input())
hs = list(map(int, input().split()))

dp = [0 for i in range(N+1)]

dp[2] = abs(hs[1]-hs[0])
for i in range(3, N+1):
  dp[i] = min(abs(hs[i-1]-hs[i-2]) + dp[i-1], abs(hs[i-1]-hs[i-3]) + dp[i-2])

route = []
p = N
while True:
  route.append(p)
  if p == 1:
    break

  if dp[p-1] + abs(hs[p-1]-hs[p-2])  == dp[p]:
    p -= 1
  else:
    p -= 2

route.reverse()
print(len(route))
print(*route)
