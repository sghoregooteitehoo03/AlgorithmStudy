import sys
from collections import deque
input = sys.stdin.readline

m, s = map(int, input().split(":"))
time = (m * 60) + s
result = 0
q = deque([(0, 0, False)])
dp = [1e9] * 3601
dp[0] = 0

while q:
    t, count, is_start = q.popleft()

    if t > time:
        continue

    if dp[t] < count:
        continue
    
    dp[t] = count
    if t == time:
        result = count
        if not is_start:
            result += 1
            
        break
            
    q.append((t + 10, count + 1, is_start))
    q.append((t + 60, count + 1, is_start))
    q.append((t + 600, count + 1, is_start))

    if is_start or (not is_start and t == 0):
        q.append((t + 30, count + 1, True))
    elif not is_start and t != 0:
        q.append((t, count + 1, True))

print(result)