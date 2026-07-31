N, M = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(M)]

def solve(ab):
  sorted_ranges = sorted(ab, key=lambda x: x[1])

  left_island = sorted_ranges[0][1]
  ans = 1
  for a,b in sorted_ranges:
    if a >= left_island:
      ans += 1
      left_island = b 

  return ans

print(solve(AB))
