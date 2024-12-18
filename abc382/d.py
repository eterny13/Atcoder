N, M = map(int,input().split())
ans = []

def dfs(now, l):
  if len(l) == N:
    ans.append(" ".join(map(str, l)))
    return 
  st = 1 if len(l) == 0 else now + 10
  end = M - 10 * (N - len(l) - 1)
  for i in range(st, end+1):
    l.append(i)
    dfs(i, l)
    l.pop(-1)

dfs(1, [])
print(len(ans))
for a in ans:
  print(a)
