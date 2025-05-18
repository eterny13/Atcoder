n,m = map(int, input().split())
res = [input() for _ in range(2*n)]
cnt = [[i, 0] for i in range(2*n)]

def zyanken(id1, id2, rd, res):
  str1 = res[id1][rd]
  str2 = res[id2][rd]
  if str1 == 'G' and str2 == 'C':
    return 1
  elif str1 == 'C' and str2 == 'P':
    return 1
  elif str1 == 'P' and str2 == 'G':
    return 1
  if str1 == 'G' and str2 == 'P':
    return -1 
  elif str1 == 'C' and str2 == 'G':
    return -1 
  elif str1 == 'P' and str2 == 'C':
    return -1
  else:
    return 0

for i in range(m):
  for j in range(n):
    zyanken_res = zyanken(cnt[2*j][0], cnt[2*j+1][0], i, res)
    if zyanken_res == 1:
      cnt[2*j][1] += 1
    elif zyanken_res == -1:
      cnt[2*j+1][1] += 1
  cnt.sort(key =lambda x: (-x[1], x[0]))
  #print(cnt)

for i in range(2*n):
  print(cnt[i][0]+1)
