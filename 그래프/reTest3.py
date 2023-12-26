from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
time_table = [0] * (n + 1)
table = [0] * (n + 1)

for i in range(1, n + 1):
    a = list(map(int, input().split()))

    for j in range(len(a)):
        if a[j] == -1:
            break

        if j == 0:
            time_table[i] = a[j]
        else:
            graph[a[j]].append(i)
            table[i] += 1

def sort():
    queue = deque()
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        if table[i] == 0:
            queue.append(table[i])
    
    while(queue):
        now = queue.popleft()
        for i in graph[now]:
            result[i] += time_table[i]
            table[i] -= 1
            
            if table[i] == 0:
                queue.append(i)

    for i in range(1, n + 1):
        print(result[i])

sort()