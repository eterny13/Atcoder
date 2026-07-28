from collections import deque

N, M = map(int, input().split())

cups = []
sstatus = [0] * (N+1)
dist = [-1] * (3**N)

for i in range(3):
  c = list(map(int, input().split()))
  cups_n = c[0]
  cups = c[1:]

  for cup in cups:
    sstatus[cup] = i

def encode(status):
  val = 0
  for i in range(1, N+1):
    val = val*3+ status[i]
  return val

def decode(val):
  status = [0] * (N+1)
  for i in range(N, 0, -1):
    status[i] = val%3
    val //= 3
  return status

goalA = encode([0] * (N+1))
goalC = encode([2] * (N+1))

start_code = encode(sstatus)
dist[start_code] = 0

q = deque([start_code])

ans = -1
while q:
  cur_code = q.popleft()
  cur_step = dist[cur_code]

  if cur_code == goalA or cur_code == goalC:
    ans = cur_step
  
  if cur_step >= M:
    continue
  
  status = decode(cur_code)

  top = [-1,-1,-1]
  for cup in range(1, N+1):
    tray = status[cup]
    top[tray] = cup
  
  pairs = [(0,1),(1,2)]

  for t1,t2 in pairs:
    c1 = top[t1]
    c2 = top[t2]

    if c1 != -1 and (c2 == -1 or c1 > c2):
      fromt, tot, move = t1, t2, c1
    elif c2 != -1 and (c1 == -1 or c2 > c1):
      fromt, tot, move = t2, t1, c2
    else:
      continue
    
    status[move] = tot
    next_code = encode(status)

    if dist[next_code] == -1:
      #print(tot)
      #print(decode(next_code))
      dist[next_code] = cur_step + 1
      q.append(next_code)
    
    status[move] = fromt

print(ans)
