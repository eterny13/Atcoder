s = input()
t = input()
n = len(s)
m = len(t)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
  for j in range(m+1):
    if i > 0 and j > 0 and s[i-1] == t[j-1]:
      dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
    elif i > 0 and j > 0 and s[i-1] != t[j-1]:
      dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    elif i > 0:
      dp[i][j] = i 
    elif j > 0:
      dp[i][j] = j 

print(dp[n][m])
