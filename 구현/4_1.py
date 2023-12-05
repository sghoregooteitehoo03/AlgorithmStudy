n = int(input())
str = input().split()
movement = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0],
}
currentPos = [0, 0]

for direct in str:
    move = movement[direct]
    movePos = currentPos.copy()

    movePos[0] += move[0]
    movePos[1] += move[1]

    if (movePos[0] < 0 or movePos[1] < 0):
        continue
    elif (movePos[0] > (n - 1) or movePos[1] > (n - 1)):
        continue

    currentPos = movePos

print(currentPos[0] + 1, currentPos[1] + 1)