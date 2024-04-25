import sys
from collections import deque
INF = 1e9
input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print(0)
    print(1)
else:
    visited = [INF] * (100001)
    q = deque([(n - 1, 1), (n + 1, 1), (2 * n, 1)])
    way_count = 0

    while q:
        pos, count = q.popleft()

        if pos >= 0 and pos <= 100000:
            if visited[pos] >= count:
                visited[pos] = count

                if pos == k:
                    way_count += 1

                q.append((pos - 1, count + 1))
                q.append((pos + 1, count + 1))
                q.append((2 * pos, count + 1))

    print(visited[k])
    print(way_count)