# https://school.programmers.co.kr/learn/courses/30/lessons/60062
# 모든 경우의 수를 확인
from itertools import permutations

INF = 1e9


def solution(n, weak, dist):
    answer = INF
    weak_size = len(weak)
    weak = weak + [w + n for w in weak]

    for start in range(weak_size):
        for d in permutations(dist, len(dist)):
            cnt = 1
            pos = start
            for i in range(1, weak_size):
                next_pos = start + i
                diff = weak[next_pos] - weak[pos]

                if diff > d[cnt - 1]:
                    pos = next_pos
                    cnt += 1

                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                answer = min(answer, cnt)
    if answer == INF:
        return -1

    return answer


# from itertools import permutations

# INF = 1e9
# def solution(n, weak, dist):
#     answer = INF
#     weak_size = len(weak)
#     weak = weak + [w + n for w in weak]

#     for start in range(weak_size):
#         for d in permutations(dist, len(dist)):
#             cnt = 1
#             pos = start
#             for i in range(1, weak_size):
#                 nextPos = start + i
#                 diff = weak[nextPos] - weak[pos]

#                 if diff > d[cnt - 1]:
#                     pos = nextPos
#                     cnt += 1

#                     if cnt > len(dist):
#                         break
#             if cnt <= len(dist):
#                 answer = min(answer, cnt)
#     if answer == INF:
#         return -1

#     return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# 12	[1, 5, 6, 10]	[1, 2, 3, 4]	2
# 12	[1, 3, 4, 9, 10]	[3, 5, 7]	1
# [False, True, False, False, False, True, True, False, False, False, True, False]
