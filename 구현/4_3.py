def get_index(char):
    return ord(char.lower()) - ord('a')
        
pos = input()
currentPos = [get_index(pos[0]), int(pos[1]) - 1]
possibleMovement = [[-1, -2], [1, -2], [-1, 2],[1, 2],
                    [2, -1], [2, 1], [-2, -1], [-2, 1]]
result = 0

for movement in possibleMovement:
    movePos = [currentPos[0] + movement[0], currentPos[1] + movement[1]]

    if (movePos[0] < 0 or movePos[1] < 0):
        continue
    elif (movePos[0] > 7 or movePos[1] > 7):
        continue

    result += 1

print(result)

# 답지
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
#          (-1, -2), (-1, 2), (1, -2), (1, 2)]
# result = 0

# for step in steps:
#     next_row = row + step[0]
#     next_col = column + step[1]

#     if (1 <= next_row and next_row <= 8) and (1 <= next_col and next_col <= 8):
#         result += 1

# print(result)