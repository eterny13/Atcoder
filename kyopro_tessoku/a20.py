s = input()
t = input()

dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

for i in range(len(s)+1):
  for j in range(len(t)+1):
    if i > 0 and j > 0 and s[i-1] == t[j-1]:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
    elif i > 0 and j > 0:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[len(s)][len(t)])
