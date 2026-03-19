# BFS 문제
# 효율을 위해서는 옆부분에 넘친 석유는 다시 계산 안하고 읽기만 수행해야함
# n을 일단 다 검사 함 석유가 있으면 BFS 동작
# 단 이미 계산을 한 석유면 불러와야됨
# 거쳐온 위치를 다 저장시켜서 석유양을 알림?

from collections import deque, defaultdict

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])

    oil_history = {}
    
    def search(start, id):
        count = 0
        queue = deque([start])

        while queue:
            i, j = deque.popleft(queue)
            count += 1
            land[i][j] = id
            
            if i + 1 < n and land[i + 1][j] == 1:
                queue.append((i + 1, j))
            
            if j + 1 < m and land[i][j + 1] == 1:
                queue.append((i, j + 1))

        return count

    for i in

    return answer