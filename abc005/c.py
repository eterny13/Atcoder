import bisect

T =  int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

ansl = []
j = 0
for i in range(M):
  r = B[i]
  l = B[i] - T
  found = False
  for k in range(j, N):
    if l <= A[k] <= r:
      found = True
      ansl.append(True)
      j = k+1
      break
  
  if not found:
    ansl.append(False) 
  
if len(ansl) == len(B) and all(ansl):
  print("yes")
else:
  print("no")
    