X,Y = map(int, input().split())

n = Y // X

cnt = 1 if X <= Y else 0
x = X
for i in range(1, n+1):
  x = x * 2
  if x <= Y:
    cnt += 1
  else:
    break

print(cnt)
