N = int(input())

prime = [True] * 1000010
prime[0] = False
prime[1] = False

i = 2
for i in range(2, 1010):
  j = i*2
  while(j <= N):
    prime[j] = False
    j += i

for i in range(2, N+1):
  if prime[i] == True:
    print(i)
