# https://www.acmicpc.net/problem/2887
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

n = int(input())
x = []
y = []
z = []
edges = []

parent = [0] * n
result = 0

for i in range(n):
    parent[i] = i

for i in range(n):
    x_data, y_data, z_data = map(int, input().split())
    
    x.append((x_data, i))
    y.append((y_data, i))
    z.append((z_data, i))

x.sort()
y.sort()
z.sort()

for i in range(len(x) - 1):
    edges.append((abs(x[i][0] - x[i + 1][0]), x[i][1], x[i + 1][1]))
    edges.append((abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]))
    edges.append((abs(z[i][0] - z[i + 1][0]), z[i][1], z[i + 1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
