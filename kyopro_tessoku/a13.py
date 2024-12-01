N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
  l = i
  r = N
  mid = 0
  while(r - l > 1):
    mid = (l+r) // 2
    if abs(A[i] - A[mid]) <= K:
      l = mid
    else:
      r = mid

  ans += abs(i - l)

print(ans)
