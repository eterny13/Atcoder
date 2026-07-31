from collections import deque

def encode(status):
  val = 0
  for i in range(1, N+1):
    val = val*3 + status[i]
  return val

def decode(val):
  status = [0] * (N+1)
  for i in range(N, 0, -1):
    status[i] = val % 3
    val //= 3
  
  return status


N, M = map(int, input().split())

cups = []
start_status = [0] * (N+1)
dist = [-1] * (3**N)

for i in range(3):
  c = list(map(int, input().split()))
  num_cups = c[0]
  cups = c[1:]

  for c in cups:
    start_status[c] = i


goalA = encode([0] * (N+1))
goalC = encode([2] * (N+1))

start_code = encode(start_status)
dist[start_code] = 0

q = deque([start_code])

ans = -1

while q:
  current_code = q.popleft()
  current_steps = dist[current_code]

  if current_code == goalA or current_code == goalC:
    ans = current_steps
  
  current_status = decode(current_code)

  if current_steps >= M:
    continue

  top = [-1,-1,-1]
  for cup in range(1, N+1):
    tray = current_status[cup]
    top[tray] = cup
  
  ### 0=A, 1=B, 2=C
  pairs = [(0,1), (1,2)]

  for t1, t2 in pairs:
    c1 = top[t1]
    c2 = top[t2]
  
    ### 左カップから右へ一番上のcupを動かす
    if c1 != -1 and (c2 == -1 or c1 > c2):
      from_t, to_t, move_c = t1, t2, c1
    ### 右から左
    elif c2 != -1 and (c1 == -1 or c2 > c1):
      from_t, to_t, move_c = t2, t1, c2
    else:
      continue
    
    current_status[move_c] = to_t
    next_code = encode(current_status)

    if dist[next_code] == -1:
      dist[next_code] = current_steps + 1
      q.append(next_code)

    ### もとに戻す 
    current_status[move_c] = from_t

print(ans)
