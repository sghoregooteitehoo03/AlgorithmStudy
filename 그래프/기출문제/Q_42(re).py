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

G = int(input())
P = int(input())

gate = [0] * (G + 1)
plain = []
result = 0

for i in range(1, G + 1):
    gate[i] = i

for _ in range(P):
    data = find_parent(gate, int(input()))
    if data == 0:
        break
    
    union_parent(gate, data, data - 1)
    result += 1

print(result)
