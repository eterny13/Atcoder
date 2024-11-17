N = int(input())
A = list(map(int, input().split()))
D = int(input())
lr = [list(map(int,input().split())) for _ in range(D)]

acc = [0 for _ in range(len(A)+1)]
for i in range(N):
  acc[i+1] += max(A[i], acc[i])

rcc = [0 for _ in range(len(A)+1)]
for i in reversed(range(0, N-1)):
  rcc[i] += max(A[i], rcc[i+1])

for i in range(D):
  print(max(acc[lr[i][0] - 1], rcc[lr[i][1]]))

#print(acc)
#print(rcc)