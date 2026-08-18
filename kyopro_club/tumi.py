import bisect

N = int(input())

ws = []
for i in range(N):
  w = int(input()) 
  ws.append(w) 

D = []

for w in ws: 

  idx = bisect.bisect_left(D, w)

  if idx < len(D):
    D[idx] = w
  else:
    D.append(w)
    D.sort()

print(len(D))
