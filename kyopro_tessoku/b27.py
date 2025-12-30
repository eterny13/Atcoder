A,B = map(int, input().split())

a = max(A,B)
b = min(A,B)

while(a % b != 0):
  v = a % b
  if v != 0:
    a = b
    b = v

gcd = b
lcm = A * B // gcd
print(lcm)
