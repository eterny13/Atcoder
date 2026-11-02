from collections import defaultdict
N, D = map(int, input().split())

dp = {1: 1.0}

for i in range(N):
  nx = defaultdict(float)

  for d, p in dp.items():
    if d == 0:
      nx[0] += p
    else:
      for j in range(1,7):
        nx[(d*j)%D] += p / 6.0
  
  dp = nx

print("%0.8f" % dp.get(0, 0.0))
