from queue import Queue

H,W = map(int, input().split())

ss = []
q = Queue()
for i in range(H):
  s = input()

  idxs = [j for j, e in enumerate(s) if e == '#']
  for j in idxs:
    q.put((i,j,0))
    #print(i, j)
  ss.append(s)

ds = [(0,1),(0, -1), (1,0), (-1,0)]
visited = [[False] * W for _ in range(H)]

ans = -1
while q.qsize() > 0:
  y,x,s = q.get()

  ans = max(ans, s)

  for dy,dx in ds:
    ny,nx = dy+y, dx+x
    if 0 <= ny < H and 0 <= nx < W and ss[ny][nx] != '#' and not visited[ny][nx]:
      visited[ny][nx] = True
      q.put((ny,nx,s+1))


print(ans)
