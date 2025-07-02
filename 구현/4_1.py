n = int(input())
movements = list(input().split())
move_map = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
current_pos = (1, 1)

for move in movements:
    move_pos = move_map[move]
    
    next_pos_y = current_pos[0] + move_pos[0]
    next_pos_x = current_pos[1] + move_pos[1]

    if (next_pos_x < 1) or (next_pos_x > n) or (next_pos_y < 1) or (next_pos_y > n):
        continue

    current_pos = (next_pos_y, next_pos_x)

print(current_pos)