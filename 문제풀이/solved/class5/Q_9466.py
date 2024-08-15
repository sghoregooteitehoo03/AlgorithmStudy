import sys
input = sys.stdin.readline

t = int(input())

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

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = n
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i

    for i in range(n):
        node = arr[i]
        
        if i + 1 == node:
            parent[i + 1] = node
            result -= 1
        else:
            if find_parent(parent, i + 1) != find_parent(parent, node):
                union_parent(parent, i + 1, node)
            else:
                parent_node = find_parent(parent, i + 1)
                for j in range(parent_node, n + 1):
                    if parent_node == parent[j]:
                        result -= 1
    
    print(result)
