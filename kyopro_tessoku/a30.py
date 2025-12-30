n,r = map(int, input().split())

modulo = 10**9 + 7

a = 1
for i in range(1, n+1):
  m = (m*i) % modulo

a = 1
for i in range(1, r+1):
  a = (a*i) % modulo

other = n-r
for i in range(1, other+1):
  a = (a*i) % modulo

ans = m * pow(a, modulo-2, modulo) % modulo
print(ans)
