n, m, b = map(int, input().split())
map_graph = []
blocks = {}

for i in range(n):
    map_graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if blocks.get(map_graph[i][j]) == None:
            blocks[map_graph[i][j]] = 1
        else:
            blocks[map_graph[i][j]] += 1

result = (1e9, -1)
sorted_key = list(blocks.keys())
sorted_key.sort(reverse=True)
for key in range(max(sorted_key), -1, -1):
    time = 0
    block = b
    is_empty = False

    for other_key in sorted_key:
        if key == other_key:
            continue

        if key < other_key:
            diff = other_key - key

            block += diff * blocks[other_key]
            time += (2 * diff * blocks[other_key])
        else:
            diff = key - other_key
            
            if block < diff * blocks[other_key]:
                is_empty = True
                break
            
            block -= diff * blocks[other_key]
            time += diff * blocks[other_key]
    
    if result[0] > time and not is_empty:
        result = (time, key)

print(result[0], end=' ')
print(result[1])