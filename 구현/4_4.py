def turnLeft(_viewIndex):
    if _viewIndex - 1 < 0:
        return 3
    else:
        return _viewIndex - 1

n, m = map(int, input().split())
posY, posX, viewIndex = map(int, input().split())
visited = [[False] * n for _ in range(m)]
mapList = []

for i in range(m):
    mapList.append(list(map(int, input().split())))

movements = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]
visited[posY][posX] = True
result = 1
turnCount = 0

while True:
    viewIndex = turnLeft(viewIndex)
    moveY = posY + movements[viewIndex][0]
    moveX = posX + movements[viewIndex][1]

    if turnCount == 4:
        break

    if (moveY < 0 or moveX < 0):
        continue
    elif (moveX > m or moveY > m):
        continue

    if mapList[moveY][moveX] == 0 and (not visited[moveY][moveX]):
        result += 1
        turnCount = 0
        posX = moveX
        posY = moveY

        visited[moveY][moveX] = True
    else:
        turnCount += 1
        
        if turnCount == 4:
            newIndex = turnLeft(turnLeft(viewIndex))
            newY = movements[newIndex][0]
            newX = movements[newIndex][1]
        
            if mapList[newY][newX] == 1:
                break
            else:
                posX = moveX
                posY = moveY
                turnCount = 0

print(result)


# 답지
# n, m = map(int, input().split())
# d = [[0] * m for _ in range(n)]
# x, y, dicrection = map(int, input().split())
# d[x][y] = 1

# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]


# def turnLeft():
#     global dicrection
#     dicrection -= 1
#     if dicrection == -1:
#         dicrection = 3


# count = 1
# turn_time = 0
# while True:
#     turnLeft()
#     nx = x + dx[dicrection]
#     ny = y + dy[dicrection]
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count +=1
#         turn_time = 0
#         continue
#     else:
#         turn_time += 1

#     if turn_time == 4:
#         nx = x - dx[dicrection]
#         ny = y - dy[dicrection]

#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         else:
#             break
#         turn_time = 0

# print(count)