A,B = map(int, input().split())

X = max(A,B)
Y = min(A,B)

ans = Y

while(X % Y != 0):
  v = X % Y
  if v != 0:
    X = Y
    Y = v


print(Y)
