
N = int(input())

L = []
for i in range(N):
    l = list(map(int, input().split()))
    L.append(l[1:])

X,Y = map(int, input().split())

print(L[X-1][Y-1])
