def solution(n, weak, dist):
    distance_dict = {}
    sorted_dist = sorted(dist, reverse=True)

    for i in range(len(weak) - 1):
        inner_dict = {}
        for j in range(i + 1, len(weak)):
            if i == j:
                continue

            inner_dict[weak[j]] = weak[j] - weak[i]
        
        distance_dict[weak[i]] = inner_dict

    for i in range(len(weak) - 1):
        for j in range(len(weak) - 1, i, -1):
            if i == j:
                continue
            
            distance = n - weak[j] + weak[i]
            if distance > 0 and distance_dict[weak[i]][weak[j]] > distance:
                distance_dict[weak[i]][weak[j]] = distance

    result = 1e9
    for node in distance_dict.keys():
        cal = 0
        visited = [False * (len(weak) + 1)]
        index = 0

        for move_node in distance_dict[node].keys():
            
            print(move_node)

            for next_node in distance_dict.keys():
                if node == next_node:
                    continue



    print(distance_dict)



solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
solution(12, [1, 3, 4, 9, 10], [3, 5, 7])