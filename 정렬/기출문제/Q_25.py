# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    counts = [0] * 502

    for stage in stages:
        counts[stage] += 1

    person = len(stages)
    for i in range(1, N + 1):
        if person <= 0:
            answer.append((0.0, i))
            continue

        rate = counts[i] / person
        answer.append((rate, i))

        person -= counts[i]

    answer.sort(key=lambda x: (-x[0], x[1]))
    result = [x[1] for x in answer]
    return result


# def solution(N, stages):
#     answer = []
#     stage_percent = [0] * (N + 2)
#     previous = 0

#     for stage in stages:
#         stage_percent[stage] += 1

#     for i in range(len(stage_percent)):
#         if i > N:
#             continue
#         elif stage_percent[i] == 0:
#             if i > 0 and i <= N:
#                 answer.append((0, i))
#             continue

#         fail_percent = stage_percent[i] / (len(stages) - previous)
#         print(fail_percent)
#         answer.append((fail_percent, i))

#         previous += stage_percent[i]

#     answer.sort(key=lambda x: (-x[0], x[1]))
#     for i in range(len(answer)):
#         answer[i] = answer[i][1]

#     return answer
