A = input()

if len(A) > 1:
  print(A[:-1])
else:
  if A[0] != 'a':
    print("a")
  else:
    print(-1)
