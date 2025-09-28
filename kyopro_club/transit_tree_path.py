from collections import deque

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
  a,b,c = map(int, input().split())
  a-=1
  b-=1
  tree[a].append([b,c])
  tree[b].append([a,c])

q,k = map(int, input().split())
queries = []
for _ in range(q):
  a,b = map(int, input().split())
  a-=1
  b-=1
  queries.append([a,b])
k-=1
parents = [-1] * n
cost_to_k = [0] * n

Q = deque()
Q.append(k)
while Q:
  now = Q.popleft()
  for child, dist in tree[now]:
    if parents[child] == -1:
      if now == k:
        parents[child] = child
      else:
        parents[child] = now
      Q.append(child)
      cost_to_k[child] = cost_to_k[now] + dist

for a,b in queries:
  print(cost_to_k[a] + cost_to_k[b])
