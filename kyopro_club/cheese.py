from collections import deque

ds = [(-1,0), (1,0), (0,-1), (0,1)]
H,W,N = map(int, input().split())

bd = []
sx = 0
sy = 0
for i in range(H):
  b = input()
  if 'S' in b:
    sy = i 
    sx = b.index('S')
  bd.append(b)


ans = 0
visited = [[-1] * W for _ in range(H)]

for i in range(N):
  q = deque()
  q.append((sy, sx, 0))
  target = str(i+1)
  visited[sy][sx] = i+1 

  while q:
    cy, cx, cs = q.popleft()

    if bd[cy][cx] == target:
      ans += cs
      sy, sx = cy, cx
      break

    for dx, dy in ds:
      nx = dx + cx
      ny = dy + cy
      if 0 <= nx < W and 0 <= ny < H and bd[ny][nx] != 'X' and visited[ny][nx] != i+1:
        visited[ny][nx] = i+1
        q.append((ny, nx, cs+1))

print(ans)
