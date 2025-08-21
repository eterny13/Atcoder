import math

N = int(input())

xs = []
ys = []

for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)


ans = 0.0
for i in range(N):
    for j in range(i+1, N):
       ax = abs(xs[i] - xs[j]) 
       ay = abs(ys[i] - ys[j])
       dist = math.sqrt(ax*ax + ay*ay)
       ans = max(dist, ans)

print("%.8f" % ans)

