MOD = 10**9+7
N, M = map(int, input().split())

killA = list(map(int, input().split()))
killB = list(map(int, input().split()))

def solve(A, B):
  n = len(A)
  # Bのキル数がデス数
  deaths = sum(B)
  same = [0] * n
  same[-1] = 1
  for i in range(n-2, -1, -1):
    if A[i] == A[i+1]:
      same[i] = same[i+1]+1
    else:
      same[i] = 1
    
  dp = [0] * (deaths + 1)
  dp[0] = 1
  #print(same)

  for i in range(n):
    dp2 = [0] * (deaths + 1)
    for j in range(deaths+1):
      for k in range(0, deaths+1-j, same[i]):
        dp2[j+k] += dp[j]
        dp2[j+k] %= MOD
    #print(dp2)
    dp = dp2

  return dp[-1]


ans = solve(killA, killB) * solve(killB, killA) % MOD
print(ans)

"""
デス数を全探索
sameは同じキル数の連続
dpテーブルはデス数のパターン
最初の入力例

連続数は [4,3,2,1]　デス数5
dp: [1, 0, 0, 0, 0, 0]
dp: [1, 0, 0, 0, 1, 0]  連続数4は[1,1,1,1] は可能
dp: [1, 0, 0, 1, 1, 0]  連続数3は[0,1,1,1] は可能
dp: [1, 0, 1, 1, 2, 1]  連続数2は[0,0,1,1] [0,0,2,2] 5デスは[0,1,1,1] + [0,0,1,1]が可能
dp: [1, 1, 2, 3, 5, 6]  連続数1は１デス[0,0,0,1] ２デス[0,0,1,1], [0,0,0,2] 3デス [0,1,1,1] [0,0,1,2], [0,0,0,3]
                         ... 

連続数 [1,3,2,1] です4
dp: [1,0,0,0,0]
dp: [1,1,1,1,1]
dp: [1,1,1,2,2] デス4は[0,0,0,1]+[0,1,1,1]                         
dp: [1,1,2,3,4] 
dp: [1,2,4,7,11]    
"""
