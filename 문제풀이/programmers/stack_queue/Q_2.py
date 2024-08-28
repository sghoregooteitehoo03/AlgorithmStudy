import math

def solution(progresses, speeds):
    answer = []
    left_days = []

    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]

        left_days.append(math.ceil((100 - progress) / speed))

    previous_value = left_days[0]
    count = 1
    for i in range(1, len(progresses)):
        if previous_value >= left_days[i]:
            count += 1
        else:
            answer.append(count)

            count = 1
            previous_value = left_days[i]
    answer.append(count)
        
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))
print(solution([90, 90, 90], [1, 5, 4]))