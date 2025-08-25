import bisect

N = int(input())
A = list(map(int, input().split()))

s = sorted(set(A))

b = []
for a in A:
  pos = bisect.bisect_left(s, a)
  b.append(pos+1)

print(*b)
