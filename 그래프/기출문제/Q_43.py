# 크루스칼 알고리즘 사용
# 비용이 낮은 순대로 연결
# 사이클이 발생하면 패스 발생하지 않으면 연결
# 연결하면서의 비용을 출력

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

n, m = map(int, input().split())
parent = [i for i in range(n)]
roads = []

total = 0
for _ in range(m):
    a, b, length = map(int, input().split())
    total += length
    roads.append((length, a, b))

roads.sort()
result = 0
for road in roads:
    length, a, b = road

    if find_parent(parent, a) == find_parent(parent, b):
        continue

    result += length
    union_parent(parent, a, b)

print(total - result)