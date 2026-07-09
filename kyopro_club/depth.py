import sys
sys.setrecursionlimit(10**6)

ds = [(1,0),(-1,0),(0,1),(0,-1)]
def dfs(y, x):
  visited[y][x] = True

  for dx,dy in ds:
    nx = x + dx
    ny = y + dy
    if 0 <= ny < H and 0 <= nx < W:
      if b[ny][nx] == 'g':
        return True

      if b[ny][nx] == '.' and not visited[ny][nx]:
        if dfs(ny, nx):
          return True
    
  return False

H, W = map(int, input().split())
visited = [[False] * W for _ in range(H)]

b = []
for _ in range(H):
  s = input()
  b.append(s)

ans = False
for i in range(H):
  for j in range(W):
    s = b[i][j]

    if s == 's':
      ans = dfs(i, j)

if ans:
  print("Yes")
else:
  print("No")