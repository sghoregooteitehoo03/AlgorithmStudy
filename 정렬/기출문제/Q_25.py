# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    stage_percent = [0] * (N + 2)
    previous = 0

    for stage in stages:
        stage_percent[stage] += 1
    
    for i in range(len(stage_percent)):
        if i > N:
            continue
        elif stage_percent[i] == 0:
            if i > 0 and i <= N:
                answer.append((0, i))
            continue
        
        fail_percent = stage_percent[i] / (len(stages) - previous)
        print(fail_percent)
        answer.append((fail_percent, i))

        previous += stage_percent[i]

    answer.sort(key=lambda x: (-x[0], x[1]))
    for i in range(len(answer)):
        answer[i] = answer[i][1]

    return answer

# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
# solution(4, [4,4,4,4,4])
solution(5, [1, 1, 1, 2, 3, 4])