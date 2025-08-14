from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
costs = [0] * (n + 1)
result = [0] * (n + 1)

for i in range(1, n + 1):
    study = list(map(int, input().split()))
    
    costs[i] = study[0]
    for j in range(1, len(study) - 1):
        graph[study[j]].append(i)
        indegree[i] += 1

q = deque([])
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        q.append((i, costs[i]))
        
while q:
    node, cost = q.popleft()
    result[node] = max(result[node], result[node] + cost)
    
    for next_node in graph[node]:
        indegree[next_node] -= 1
        
        if indegree[next_node] == 0:
            q.append((next_node, costs[next_node] + cost))

for i in range(1, len(result)):
    print(result[i])