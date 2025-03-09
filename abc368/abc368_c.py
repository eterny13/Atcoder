# coding: utf-8
# Your code here!
N = map(int, input().split())
H = map(int, input().split())

cnt = 0
for h in H:
    c = h // 5
    cnt += c*3
    
    hh = h%5
    while(hh>=1):
        if(hh>=3):
            cnt+=3
        else:
            hh-=1
            cnt+=1

print(cnt)

