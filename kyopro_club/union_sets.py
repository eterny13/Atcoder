import sys

def find_at_time(i, t):
    while parent[i] != i:
        if times[i] > t:
            break
        i = parent[i]
    
    return i

def unite(u,v,t):
    root_u = find_at_time(u, t)
    root_v = find_at_time(v, t)

    if root_u == root_v:
        return False
    
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
        times[root_u] = t
    else:
        parent[root_v] = root_u
        times[root_v] = t

        if rank[root_u] == rank[root_v]:
            rank[root_u] += 1
    
    return True

N,M = list(map(int, input().split()))

parent = list(range(N+1))
### 木の高さ
rank = [1] * (N+1)
times = [0] * (N+1)

for i in range(M):
    a,b = list(map(int, input().split()))
    unite(a,b,i+1)

Q = int(input())

for i in range(Q):
    x,y = list(map(int, input().split()))

    if find_at_time(x, M) != find_at_time(y, M):
        print(-1)
        continue 
    
    ng = 0
    ok = M

    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2

        if find_at_time(x, mid) == find_at_time(y, mid):
            ok = mid
        else:
            ng = mid

    print(ok)
