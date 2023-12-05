from collections import deque

def bfs(graph, start, visited, movements):
    visited[0][0] = True
    result = [[1] * m for _ in range(n)]
    queue = deque([start])

    while queue:
        currentPos = queue.popleft()
        dy = currentPos[0]
        dx = currentPos[1]

        if dy == len(graph) - 1 and dx == len(graph[0]) - 1:
            print(result[dy][dx])
            break

        for movement in movements:
            nextMove = [currentPos[0] + movement[0], currentPos[1] + movement[1]]
            nextDy = nextMove[0]
            nextDx = nextMove[1]

            if (nextDy < 0 or nextDx < 0):
                continue
            elif (nextDy > len(graph) - 1 or nextDx > len(graph[0]) - 1):
                continue

            if graph[nextDy][nextDx] == '1' and not visited[nextDy][nextDx]:
                queue.append([nextDy, nextDx])
                visited[nextDy][nextDx] = True
                
                result[nextDy][nextDx] = result[dy][dx] + 1
    

n, m = map(int, input().split())
room = []
visited = [[False] * m for _ in range(n)]
movements = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
    inputData = input()
    room.append(inputData)

bfs(room, [0, 0], visited, movements)