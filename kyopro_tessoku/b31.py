N = int(input())

N3 = N//3
N5 = N//5
N7 = N//7
N15 = N//15
N21 = N//21
N35 = N//35
N105 = N//105

ans = N3 + N5 + N7 - N15 - N21 - N35 + N105
print(ans)
