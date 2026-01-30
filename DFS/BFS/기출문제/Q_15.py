# https://www.acmicpc.net/problem/18352
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
answers = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    queue = deque([start])

    while queue:
        q = queue.popleft()
        if visited[q[0]]:
            continue
        
        visited[q[0]] = True
        if q[1] == k:
            answers.append(q[0])
            continue

        for node in graph[q[0]]:
            queue.append((node, q[1] + 1))

bfs((x, 0))
if len(answers) == 0:
    print(-1)
else:
    answers.sort()
    for i in range(len(answers)):
        print(answers[i])

# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# distance = [1e9] * (n + 1)
# visited = [False] * (n + 1)

# for i in range(m):
#     city, other_city = map(int, input().split())
#     graph[city].append(other_city)

# def BFS(graph, visited, start, distance):
#     q = deque()
    
#     q.append((start, 0))
#     visited[start] = True
#     distance[start] = 0

#     while(q):
#         node, cost = q.popleft()

#         for n in graph[node]:
#             if not visited[n]:
#                 distance[n] = cost + 1
#                 visited[n] = True
#                 q.append((n, distance[n]))

# BFS(graph, visited, x, distance)

# is_empty = True
# for i in range(n + 1):
#     if distance[i] == k:
#         is_empty = False
#         print(i)

# if(is_empty):
#     print(-1)