N =int(input())

AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(N)]

CD.sort(key=lambda x: x[0])

ans = 0
visited = [False] * N

for bx,by in CD:
  max_y = -1
  max_idx = -1

  for i in range(N):
    if not visited[i]:
      rx,ry = AB[i]
      if rx < bx and ry < by:
        if ry > max_y:
          max_y = ry
          max_idx = i
    
  if max_idx != -1:
    CD[max_idx]
    visited[max_idx] = True
    ans += 1

print(ans)
