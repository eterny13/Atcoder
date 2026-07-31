N = int(input())

vs = [list(map(int, input().split())) for _ in range(N)]

sorted_vs = sorted(vs, key=lambda x: x[0] - x[1])
sorted_vs.reverse()

st = sorted_vs[0][0] - sorted_vs[0][1]

ans = 1
for x, w in sorted_vs:
  rg = x + w

  if st >= rg:
    ans += 1
    st = x - w 
  
print(ans)
