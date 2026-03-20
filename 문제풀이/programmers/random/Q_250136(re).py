# BFS 문제
# 효율을 위해서는 옆부분에 넘친 석유는 다시 계산 안하고 읽기만 수행해야함
# n을 일단 다 검사 함 석유가 있으면 BFS 동작
# 단 이미 계산을 한 석유면 불러와야됨
# 거쳐온 위치를 다 저장시켜서 석유양을 알림?

from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    col_oil_sum = [0] * m
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True

                size = 0
                cols_in_chunk = set()

                while queue:
                    x, y = queue.popleft()
                    size += 1
                    cols_in_chunk.add(y)

                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]

                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                
                for col in cols_in_chunk:
                    col_oil_sum[col] += size
    
    return max(col_oil_sum)


print(
    solution(
        [
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1],
        ]
    )
)
