import math
a,b = map(int, input().split())

c = math.sqrt(a*a + b*b)

print('{:.10f} {:.10f}'.format(a/c, b/c))
