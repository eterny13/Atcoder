N,M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

st = 200010
ids = [-1 for _ in range(st)]

s = st
for i, a in enumerate(A):
  while(s > a):
    s-=1
    ids[s] = i+1

for b in B:
  print(ids[b])
