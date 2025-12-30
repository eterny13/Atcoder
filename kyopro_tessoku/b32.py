n,k = map(int, input().split())

A = list(map(int, input().split()))

dp = [False] * (n+1)

for i in range(n+1):
  for a in A:
    if i >= a and dp[i-a] is False:
      dp[i] = True
      break
  

if dp[n] is False:
  print("Second")
else:
  print("First")
