
N,M = list(map(int, input().split()))
K = []

for _ in range(M):
    k = list(map(int, input().split()))
    K.append(k[1:])

P = list(map(int , input().split()))



ans = 0
for i in range(1<<N):
    l = []
    for j in range(M):
        c = 0
        for k in K[j]:
            n = (i >> (k-1)) % 2
            if n == 1:
                c+=1
        
        if c % 2 == P[j]:
            l.append(True)
        else:
            l.append(False)
    
    if all(l):
        ans += 1

print(ans)
