# 서로소 확인
# 그래프 간 유니온 수행
# 여행계획의 부모노드가 모두 같으면 YES, 그게 아니면 NO

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
parent = [i for i in range(n + 1)]

for i in range(n):
    connections = list(map(int, input().split()))
    for j in range(len(connections)):
        if connections[j] == 0:
            continue
        union_parent(parent, i + 1, j + 1)

visit_plan = list(map(int, input().split()))
is_success = True
for i in range(1, len(visit_plan)):
    if find_parent(parent, visit_plan[i - 1]) != find_parent(parent, visit_plan[i]):
        is_success = False
        break

if is_success:
    print("YES")
else:
    print("NO")

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])

#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# n, m = map(int, input().split())
# map_table = []
# parent = [0] * n

# for i in range(n):
#     map_table.append(list(map(int, input().split())))
#     parent[i] = i

# plan = list(map(int, input().split()))

# for i in range(n):
#     for j in range(n):
#         if map_table[i][j] == 1:
#             if find_parent(parent, i) != find_parent(parent, j):
#                 union_parent(parent, i, j)

# result = 'YES'
# for i in range(n - 1):
#     if parent[i] != parent[i + 1]:
#         result = 'NO'
#         break

# print(result)
