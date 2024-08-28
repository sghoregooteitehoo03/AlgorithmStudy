def solution(genres, plays):
    answer = []
    file = {}
    sort_key = []

    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]

        if file.get(genre) == None:
            file[genre] = [(play_count, i)]
        else:
            file[genre].append((play_count, i))

    for key in file.keys():
        play_count_sum = 0
        for play_count, _ in file[key]:
            play_count_sum += play_count
    
        file[key].sort(key=lambda x : x[0], reverse=True)
        sort_key.append((play_count_sum, key))
    sort_key.sort(key=lambda x : x[0], reverse=True)
    
    for _, key in sort_key:
        count = 0
        
        for _, index in file[key]:
            if count == 2:
                break
            answer.append(index)
            count += 1

    return answer

answer = solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
print(answer)
