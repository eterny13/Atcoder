
bd = []
for _ in range(10):
  s = input().strip()
  bd.append(list(s))

ds = [(1,0),(-1,0),(0,1),(0,-1)]
def dfs(y,x,c):
  visited[y][x] = True

  for dy,dx in ds:
    ny = y + dy
    nx = x + dx
    if 0 <= ny < 10 and 0 <= nx < 10:
      if bd[ny][nx] == 'o' and visited[ny][nx] is False:
        c = dfs(ny, nx, c+1)
  
  return c

ct = 0
for i in range(10):
  for j in range(10):
    if bd[i][j] == 'o':
      ct += 1

ans = False
for i in range(10):
  for j in range(10):
    if bd[i][j] == 'x':
      visited =[[False] * 10 for _ in range(10)]
      bd[i][j] = 'o'
      cc = dfs(i,j,0)
      #print(cc)
      if cc == ct:
        ans = True
      bd[i][j] = 'x'

print("YES" if ans else "NO")
