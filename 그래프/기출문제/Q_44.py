# https://www.acmicpc.net/problem/2887
# 크루스칼 알고리즘 적용
# 각 행성마다의 터널 연결 비용을 계산해서 배열에 저장
# 배열 정렬
# 정렬시킨 배열을 기준으로 union 수행
# 드는 비용 출력

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


n = int(input())
parent = [i for i in range(n)]
x_info = []
y_info = []
z_info = []

for i in range(n):
    x, y, z = map(int, input().split())
    x_info.append((x, i))
    y_info.append((y, i))
    z_info.append((z, i))

x_info.sort()
y_info.sort()
z_info.sort()

graph = []
for i in range(1, n):
    graph.append((abs(x_info[i - 1][0] - x_info[i][0]), x_info[i - 1][1], x_info[i][1]))
    graph.append((abs(y_info[i - 1][0] - y_info[i][0]), y_info[i - 1][1], y_info[i][1]))
    graph.append((abs(z_info[i - 1][0] - z_info[i][0]), z_info[i - 1][1], z_info[i][1]))

graph.sort()
result = 0
for g in graph:
    cost, a, b = g

    if find_parent(parent, a) == find_parent(parent, b):
        continue

    union_parent(parent, a, b)
    result += cost

print(result)
