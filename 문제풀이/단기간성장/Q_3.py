r, c = map(int, input().split())
map_graph = []
l_pos1 = -1
l_pos2 = -1

for i in range(r):
    map_graph.append(list(input()))

is_break = False
for i in range(r):
    for j in range(c):
        if map_graph[i][j] == 'L':
            if l_pos1 == -1:
                l_pos1 = (i, j)
                break
            else:
                l_pos2 = (i, j)
                is_break = True
                break
    
    if is_break:
        break

print(l_pos1)
print(l_pos2)
print(map_graph)