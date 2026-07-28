
n = int(input())
N = 1000 - n

coins = [500, 100, 50, 10, 5, 1]

target = N
ans = 0
for i in range(6):
  num = target // coins[i]
  target -= num * coins[i]
  ans += num

print(ans)
