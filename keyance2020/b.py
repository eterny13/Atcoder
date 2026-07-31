N = int(input())

xls = [list(map(int, input().split())) for _ in range(N)]


def solve(xls):
  sorted_ranges = sorted(xls, key=lambda x: x[0] + x[1])

  x, l = sorted_ranges[0]
  arm_range = x+l
  ans = 1

  for x, l in sorted_ranges:
    sp = x - l

    if sp >= arm_range:
      ans += 1
      arm_range = x+l
  
  return ans

print(solve(xls))
