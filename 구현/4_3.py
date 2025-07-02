current_pos = input()
current_pos = (int(current_pos[1]), ord(current_pos[0]) - 96)
movements = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

count = 0

for move in movements:
    next_pos_y = current_pos[0] + move[0]
    next_pos_x = current_pos[1] + move[1]

    if(next_pos_x > 0 and next_pos_x <= 8 and next_pos_y > 0 and next_pos_y <= 8):
        count += 1

print(count)