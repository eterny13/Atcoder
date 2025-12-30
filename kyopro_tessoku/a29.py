a,b = list(map(int, input().split()))

def Power(a,b,m):
  ans = 1
  p = a

  for i in range(60):
    wari = 1 << i
    if (b // wari) % 2 == 1:
      ans = (ans * p) % m
    p = (p * p) % m
  
  return ans

print(Power(a,b, 10**9+7))
