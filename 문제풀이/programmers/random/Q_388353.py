from copy import deepcopy
from collections import deque

def car(storage, remove_container):
    new_storage = deepcopy(storage)
    n = len(storage)
    m = len(storage[0])
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0)])
    to_remove = set()

    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                if storage[i][j] == "":
                    queue.append((i, j))
                    visited[i][j] = True
                elif storage[i][j] == remove_container:
                    to_remove.add((i, j))
                    visited[i][j] = True

    while queue:
        i, j = (queue.popleft())

        for move_i, move_j in move:
            next_i = i + move_i
            next_j = j + move_j

            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                continue

            if not visited[next_i][next_j]:
                if storage[next_i][next_j] == "":
                    visited[next_i][next_j] = True
                    queue.append((next_i, next_j))
                elif storage[next_i][next_j] == remove_container:
                    visited[next_i][next_j] = True
                    to_remove.add((next_i, next_j))

    for r, c in to_remove:
        new_storage[r][c] = ""

    return (new_storage, len(to_remove))


def crain(storage, remove_container):
    new_storage = deepcopy(storage)
    n = len(storage)
    m = len(storage[0])
    remove_count = 0

    for i in range(n):
        for j in range(m):
            container = storage[i][j]

            if container == remove_container:
                new_storage[i][j] = ""
                remove_count += 1

    return (new_storage, remove_count)


def solution(storage, requests):
    answer = len(storage) * len(storage[0])
    print(answer)
    char_storage = []

    for i in range(len(storage)):
        arr = []
        for c in storage[i]:
            arr.append(c)
        char_storage.append(arr)

    for request in requests:
        if len(request) == 2:
            char_storage, count = crain(char_storage, request[0])
            answer -= count
        else:
            char_storage, count = car(char_storage, request[0])
            answer -= count

    print(char_storage)
    return answer


print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))
