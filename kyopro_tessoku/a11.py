N,X = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = len(A)

while(r-l > 1):
  mid = (l+r) // 2
  if A[mid] == X:
    print(mid+1)
    break
  elif A[mid] < X:
    l = mid
  elif A[mid] > X:
    r = mid
