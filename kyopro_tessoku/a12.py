N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = 10 ** 18

while(r-l>1):
  mid = (l+r) // 2 
  sumv = 0
  for a in A:
    sumv += mid // a 

  if sumv < K:
    l = mid
  if sumv >= K:
    r = mid

print(l+1)
