def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
map_table = []
parent = [0] * n

for i in range(n):
    map_table.append(list(map(int, input().split())))
    parent[i] = i

plan = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if map_table[i][j] == 1:
            if find_parent(parent, i) != find_parent(parent, j):
                union_parent(parent, i, j)

result = 'YES'
for i in range(n - 1):
    if parent[i] != parent[i + 1]:
        result = 'NO'
        break

print(result)
