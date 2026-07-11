from queue import Queue

H,W = map(int, input().split())

ss = []
walls = 0
for _ in range(H):
  s = input()

  walls += s.count('#')
  ss.append(s)

q = Queue()
q.put((0,0,1))
ds = [(0,1),(0, -1), (1,0), (-1,0)]
visited = [[False] * W for _ in range(H)]

step = 10**18 
while q.qsize() > 0:
  y, x, s = q.get()

  if y == H-1 and x == W-1:
    step = min(s, step)

  for dy,dx in ds:
    ny,nx = dy+y, dx+x

    if 0 <= ny < H and 0 <= nx < W and ss[ny][nx] != '#' and not visited[ny][nx]:
      visited[ny][nx] = True
      q.put((ny,nx, s+1))


if step == 10**18:
  print(-1)
else:
  print(H * W - walls - step)
