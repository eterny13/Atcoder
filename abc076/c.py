S = input()
T = input()

found = False
ans = ""
for i in range(len(S)-len(T), -1, -1):
  ok = True
  for j in range(len(T)):
    if S[i+j] != T[j] and S[i+j] != '?':
      ok = False
      break

  if ok:
    SS = S[:i]  + T + S[i+len(T):]
    ans = SS.replace('?', 'a')
    found = True
    break

print(ans if found else "UNRESTORABLE")
