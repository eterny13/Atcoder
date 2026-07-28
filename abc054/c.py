from itertools import permutations

N, M = map(int, input().split())

g = [[] for _ in range(N+1)]
for _ in range(M):
  a,b= map(int, input().split())
  g[a].append(b)
  g[b].append(a)

visited = [False] * (N+1)
ans = 0

p = [i for i in range(1, N+1)]
for c in permutations(p):
  if c[0] != 1:
    continue
  stack = [c[0]]

  visited = [False] * (N+1)
  visited[c[0]] = True
  for i in range(N-1):
    if not visited[c[i+1]] and c[i+1] in g[c[i]]:
      visited[c[i+1]] = True
  
  if all(x == True for x in visited[1:]):
    ans += 1

print(ans)
