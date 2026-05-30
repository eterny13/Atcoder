from bisect import bisect 
import math

N,K = map(int, input().split())
A = list(map(int, input().split()))

R = 10**20
L = 0

while (R-L > 1):
    m = (R+L) // 2

    count = 0
    for i in range(1, N+1):
        c = m - A[i-1]

        if c > 0:
            cc = (c + i - 1) // i
            count += cc
    
    if count > K:
        R = m
    else:
        L = m

print(L)
