from itertools import permutations

N = int(input())
K = int(input())

nums = [int(input()) for _ in range(N)]

cnum = set()
for c in permutations(nums):
  strn = ""
  for i in range(K):
    strn += str(c[i])
  cnum.add(strn)

#print(cnum)
print(len(cnum))
