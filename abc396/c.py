n, m = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))
W = sorted(list(map(int, input().split())))

B.reverse()
W.reverse()

bacc = [0 for _ in range(n+1)]
wacc = [0 for _ in range(m+1)]

for i in range(n):
  bacc[i+1] = bacc[i] + B[i]
for i in range(m):
  wacc[i+1] = max(wacc[i] + W[i], wacc[i])

ans = 0

for i in range(n+1):
  ans = max(bacc[i] + wacc[min(i, m+1)], ans)

print(ans)
