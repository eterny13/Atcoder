X,Y = map(int, input().split())

L = []
N = []
for i in range(X):
    l = list(map(int, input().split()))
    L.append(l[1:])
    N.append(l[0])

C = list(map(int, input().split()))

count = 0

ans = 0
for i in range(X):
    c = N[i] * C[i]

    if count + c >= Y:
        Y -= count
        ans = L[i][(Y-1) % len(L[i])]
        break

    count += c 

print(ans)
