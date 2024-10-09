# coding: utf-8
# Your code here!
N,S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(S+1):
        if i == 0:
            continue
        dp[i][j] = dp[i-1][j]
        if A[i-1] <= j:
            dp[i][j] = max(A[i-1] + dp[i-1][j-A[i-1]], dp[i][j])

#print(dp[N])
if S in dp[N]:
    print("Yes")
else:
    print("No")
