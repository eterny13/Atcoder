
N, M = map(int, input().split())

persons = [[0,0,0] for _ in range(M)]
dp = [[[0] * 102 for _ in range(102)] for _ in range(102)]
for i in range(N):
  a,b,c,w = map(int, input().split())
  dp[a][b][c] = max(dp[a][b][c], w)

for i in range(M):
  a,b,c = map(int, input().split())
  persons[i][0] = a
  persons[i][1] = b
  persons[i][2] = c 

for i in range(102):
  for j in range(102):
    for k in range(102):
      if i > 0:
        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
      if j > 0:  
        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k])
      if k > 0:  
        dp[i][j][k] = max(dp[i][j][k], dp[i][j][k-1])

for a,b,c in persons:
  print(dp[a][b][c])
