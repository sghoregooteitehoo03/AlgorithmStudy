# 플로이드워셜 풀이
# 각 노드끼리 union 수행
# 만들어진 parent에서 서로 다른 노드의 개수를 반환

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

def solution(n, computers):
    parent = [i for i in range(n)]
    
    for i in range(n):    
        for j in range(n):
            if i == j or computers[i][j] == 0 or find_parent(parent, i) == find_parent(parent, j):
                continue

            union_parent(parent, i, j)

    result = set()
    for p in parent:
        result.add(find_parent(parent, p))
    
    return len(result)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))