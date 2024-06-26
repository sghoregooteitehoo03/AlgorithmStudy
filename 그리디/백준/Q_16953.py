import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())
q = deque([(a, 1)])
result = -1

while q:
    number, count = q.popleft()
    
    if number == b:
        result = count
        break

    if number * 2 <= b:
        q.append((number * 2, count + 1))
    
    if (number * 10) + 1 <= b:
        q.append(((number * 10) + 1, count + 1))

print(result)