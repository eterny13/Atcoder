N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = 10 ** 9 + 1

while(l < r):
  mid = (l+r) // 2 
  sumv = 0
  for a in A:
    sumv += mid // a 

  if sumv < K:
    l = mid + 1
  if sumv >= K:
    r = mid

print(l)
