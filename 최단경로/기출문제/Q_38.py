def find_stack(dp, graph, node):
    stack_result = 0
    if dp[node] != 0:
        return dp[node]

    if len(graph[node]) == 0:
        return 1

    for n in graph[node]:
        stack = 1 + find_stack(dp, graph, n)
        stack_result = max(stack_result, stack)

    for n in graph[node]:
        dp[n] = stack_result - 1

    return stack_result



n, m = map(int, input().split())
dp = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    val1, val2 = map(int, input().split())
    graph[val2].append(val1)

for i in range(1, n + 1):
    find_stack(dp, graph, i)

print(dp)
print(graph)

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4