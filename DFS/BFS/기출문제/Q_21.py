# https://www.acmicpc.net/problem/16234
from collections import deque

n, l, r = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))

answer = 0

while True:
    group = [[] for _ in range(n * n)]
    group[0].append((board[0][0], 0, 0))
    queue = deque([(0, 0, board[0][0], 0)])
    grouped = [[False] * n for _ in range(n)]

    is_start = True

    while queue:
        i, j, previous_value, previous_group_id = queue.popleft()

        if i < 0 or i >= len(board) or j < 0 or j >= len(board):
            continue

        current_value = board[i][j]

        if is_start or (
            abs(current_value - previous_value) >= l
            and abs(current_value - previous_value) <= r
        ):
            if not is_start and not grouped[i][j]:
                group[previous_group_id].append((current_value, i, j))
                grouped[i][j] = True

            queue.append((i + 1, j, current_value, previous_group_id))
            queue.append((i, j + 1, current_value, previous_group_id))
        else:
            queue.append((i + 1, j, current_value, previous_group_id + 1))
            queue.append((i, j + 1, current_value, previous_group_id + 1))

        if is_start:
            is_start = False

    if len(group[0]) == 1:
        break

    for g in group:
        if len(g) == 0:
            break
        sum_value = sum(t[0] for t in g)
        result = sum_value // len(g)

        for content in g:
            board[content[1]][content[2]] = result

    answer += 1
print(answer)

# from collections import deque
# import sys
# input = sys.stdin.readline

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

# n, l, r = map(int, input().split())
# map_graph = []

# for i in range(n):
#     map_graph.append(list(map(int, input().split())))

# is_moved = True
# result = -1
# parent = [0] * (n * n)

# while is_moved:
#     result += 1

#     is_moved = False
#     cal_dict = {}
#     visited = [[False] * n for _ in range(n)]
#     visited[0][0] = True

#     for i in range( n * n):
#         parent[i] = i

#     q = deque([(0, 0)])
#     while q:
#         pos_i, pos_j = q.popleft()

#         if pos_i + 1 < n:
#             if not visited[pos_i  + 1][pos_j]:
#                 visited[pos_i + 1][pos_j] = True
#                 q.append((pos_i + 1, pos_j))
#             diff = abs(map_graph[pos_i][pos_j] - map_graph[pos_i + 1][pos_j])

#             if diff >= l and diff <= r:
#                 union_parent(parent, (pos_i * n) + pos_j, ((pos_i + 1) * n) + pos_j)

#         if pos_j + 1 < n:
#             if not visited[pos_i][pos_j + 1]:
#                 visited[pos_i][pos_j + 1] = True
#                 q.append((pos_i, pos_j + 1))
#             diff = abs(map_graph[pos_i][pos_j] - map_graph[pos_i][pos_j + 1])

#             if diff >= l and diff <= r:
#                 union_parent(parent, (pos_i * n) + pos_j, (pos_i * n) + (pos_j + 1))

#     for i in range(n * n):
#         index = find_parent(parent, parent[i])
#         pos_i = i // n
#         pos_j = i % n

#         if cal_dict.get(index) == None:
#             cal_dict[index] = [(map_graph[pos_i][pos_j], pos_i, pos_j)]
#         else:
#             cal_dict[index].append((map_graph[pos_i][pos_j], pos_i, pos_j))

#     for key in cal_dict.keys():
#         if len(cal_dict[key]) == 1:
#             continue

#         is_moved = True
#         summary = 0
#         for data in cal_dict[key]:
#             summary += data[0]

#         summary = summary // len(cal_dict[key])
#         for data in cal_dict[key]:
#             map_graph[data[1]][data[2]] = summary

# print(result)
