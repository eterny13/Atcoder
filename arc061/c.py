s = input()
n = len(s)

ans = 0
for i in range(1<<(n-1)):
    cur = 0
    temps = s[0]

    for j in range(n-1):
        if (i >> j) & 1:
            cur += int(temps)
            temps = s[j+1]
        else:
            temps += s[j+1]

    cur += int(temps) 
    ans += cur

print(ans)
