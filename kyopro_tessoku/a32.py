n,a,b = map(int, input().split())

dp = [False] * (n+1)

for i in range(n+1):
  if i>=a and dp[i-a] is False:
    dp[i] = True
  elif i>=b and dp[i-b] is False:
    dp[i] = True
  else:
    dp[i] = False

if dp[n] is False:
  print("Second")
else:
  print("First")
