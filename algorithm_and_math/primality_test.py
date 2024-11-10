import math

N = int(input())

ans = "Yes"
for i in range(2, N):
  if i * i > N:
    break
  if N % i == 0:
    ans = "No"
    break

print(ans)
 