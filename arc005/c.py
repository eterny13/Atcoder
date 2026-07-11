from collections import deque

H,W = map(int, input().split())

ss = []
q = deque()
visited = [[False] * W for _ in range(H)]

for i in range(H):
  s = input()

  if 's' in s:
    j = s.index('s')
    q.append((i,j,0))
    visited[i][j] = True
  ss.append(s)

ds = [(0,1),(0, -1), (1,0), (-1,0)]

ans = "NO"
while q :
  y,x,wall = q.popleft()

  if ss[y][x] == 'g':
    ans = "YES"
  visited[y][x] = True

  for dy,dx in ds:
    ny,nx = dy+y,dx+x
    if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx]:
      if ss[ny][nx] == '#' and wall < 2:
        q.append((ny,nx,wall+1))
        #print(ny,nx,wall+1)
      
      if ss[ny][nx] != '#':
        q.appendleft((ny,nx,wall))
        #print(ny,nx,wall)
 
print(ans)
