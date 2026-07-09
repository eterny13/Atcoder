import sys
sys.setrecursionlimit(200000)

def dfs(cur, par):
  visited[cur] = True
  is_tree = True 

  for v in g[cur]:
    if v == par:
      continue
    if visited[v]:
      is_tree = False
    else:
      if not dfs(v, cur):
        is_tree = False
  
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
    if dfs(i, 0):
      ans += 1 

print(ans)
