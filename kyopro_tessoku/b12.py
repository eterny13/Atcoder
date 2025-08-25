N = int(input())

ans = 0
left = 1
right = 100
mid = 0.0

while right - left >= 0.001:
  mid = (left + right) / 2.0
  v = pow(mid, 3) + mid
  if N == v:
    break
  elif N < v:
    right = mid
  elif N > v:
    left = mid

print("%f" % mid)
