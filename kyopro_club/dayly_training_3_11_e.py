n,x,y = map(int, input().split())

red_jwls = [0 for _ in range(n)]
blue_jwls = [0 for _ in range(n)]
level = n - 1
red_jwls[level] = 1

while(level > 0):
  cntr = red_jwls[level]
  red_jwls[level] -= cntr * 1
  red_jwls[level-1] += cntr * 1
  blue_jwls[level] += cntr * x

  cntb = blue_jwls[level]
  blue_jwls[level] -= cntb * 1
  red_jwls[level-1] += cntb * 1
  blue_jwls[level-1] += cntb * y
  
  level -= 1

print(blue_jwls[0])
