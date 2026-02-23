# coding: utf-8
# Your code here!from collections import dequeu

from collections import deque

Q=deque()

S = input()

ans = []
for i in range(len(S)):
    if (S[i] == '('):  
        Q.append(i+1)
    else:
        l = Q[-1]
        ans.append([l,i+1])
        Q.pop()


for i in range(len(ans)):
    print(str(ans[i][0]) + " " + str(ans[i][1]))
