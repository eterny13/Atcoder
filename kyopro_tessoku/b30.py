h,w = map(int, input().split())

modulo = 10**9 + 7

n = h + w -2
r = h - 1 

a = 1
for i in range(1, n+1):
  a = (a*i) % modulo

b = 1
for i in range(1, r+1):
  b = (b*i) % modulo

other = n-r
for i in range(1, other+1):
  b = (b*i) % modulo

ans = a * pow(b, modulo-2, modulo) % modulo
print(ans)
