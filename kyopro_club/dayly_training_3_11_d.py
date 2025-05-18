import math
a,b,k = map(int, input().split())

ans = 0
slime = a
while(slime < b):
  slime *= k
  ans += 1

print(ans)
