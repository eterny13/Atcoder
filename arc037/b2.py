from queue import Queue

def bfs(cur):
  dq = Queue()
  dq.put(cur)
  is_tree = True

  while dq.qsize() > 0:
    c = dq.get()
    if visited[c]:
      is_tree = False
    else:
      visited[c] = True
      for v in g[c]:
        if not visited[v]:
          dq.put(v)
  
  return is_tree

N, M = map(int, input().split())

g = [[] for _ in range(N+1)]
for _ in range(M):
  u,v = map(int, input().split())
  g[u].append(v)
  g[v].append(u)

visited = [False] * (N+1)

ans = 0
for i in range(1, N+1):
  if not visited[i]:
    if bfs(i):
      ans += 1

print(ans)
