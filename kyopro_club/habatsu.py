
N,M = list(map(int, input().split()))

xys = set()
for _ in range(M):
  x,y = list(map(int, input().split()))
  xys.add((x,y))


ans = 0
for i in range(1<<N):
  members = []
  for j in range(N):
    if (i>>j) & 1:
      members.append(j+1)
    
  connected = True
  for j in range(len(members)):
    for k in range(j+1, len(members)):
      u = members[j]
      v = members[k]
      if (u,v) not in xys:
        connected  = False
    
  if connected:
    ans = max(ans, len(members))
      
print(ans)
