import bisect

N = int(input())
A = list(map(int, input().split()))

length = 0
L = []
dp = [None] * (N+1)

for i in range(N):
  pos = bisect.bisect_left(L, A[i])
  dp[i] = pos

  if dp[i] >= length:
    L.append(A[i])
    length += 1
  else:
    L[dp[i]] = A[i]

print(length)
