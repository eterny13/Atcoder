import math

N = int(input())

ans = []

def judge(n):
    flag = True
    for i in range(2, n):
        if i * i > n:
            continue
        if n % i == 0:
            flag = False
            break
    
    return flag

for i in range(2, N+1):
    if judge(i):
        ans.append(i)

ans = [str(i) for i in ans]
stra = " ".join(ans)
print(stra)
