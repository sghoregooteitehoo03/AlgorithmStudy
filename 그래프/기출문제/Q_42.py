# 서로수 문제
# 탑승구 수 만큼 parent 생성

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


g = int(input())
p = int(input())
parent = [i for i in range(g + 1)]

flow = []
for _ in range(p):
    flow.append(int(input()))

result = 0
for plain in flow:
    root = find_parent(parent, plain)

    if root != 0:
        union_parent(parent, root, root - 1)
        result += 1
    else:
        break

print(result)