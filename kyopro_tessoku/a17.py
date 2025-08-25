n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

dp[1] = A[0]
for i in range(2, n):
  dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])

ans = []
p = n
while True:
  ans.append(p)
  if p == 1:
    break
  
  if dp[p-2] + A[p-2] == dp[p-1]:
    p -= 1
  else:
    p -= 2

ans.reverse()
print(len(ans))
print(*ans)
