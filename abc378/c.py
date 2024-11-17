N = int(input())
A = list(map(int, input().split()))
memo = {}
ans = []

for i, a in enumerate(A):
  if a in memo:
    ans.append(memo[a])
    memo[a] = i+1
  else:
    ans.append(-1) 
    memo[a] = i+1

ans = " ".join([str(i) for i in ans])
print(ans)
