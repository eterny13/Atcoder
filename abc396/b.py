Q = int(input())


cards = [0 for _ in range(100)]
ans = []
for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        cards.append(query[1])
    else:
        last = cards.pop()
        ans.append(last)

for i in ans:
    print(i)
