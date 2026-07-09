import sys
sys.setrecursionlimit(200000)

def dfs(i, j):
  s = []
  ds = [(-1,-1), (-1, 0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

  s.append((i, j))
  while len(s) > 0:
    x, y = s.pop()
    visited[y][x] = True
    for dx,dy in ds:
      nx = dx + x
      ny = dy + y

      if 0 <= nx < W and 0 <= ny < H and not visited[ny][nx] and C[ny][nx] == 1:
        s.append((nx, ny))

while(True):
  W,H = map(int, input().split())
  if H == 0 and W == 0: break
  C = []
  visited = [[False] * W for _ in range(H)]

  for i in range(H):
    c = list(map(int, input().split()))
    C.append(c)

  ans = 0
  for y in range(H):
    for x in range(W):
      if not visited[y][x] and C[y][x] == 1:
        dfs(x, y)
        ans += 1

  print(ans)
