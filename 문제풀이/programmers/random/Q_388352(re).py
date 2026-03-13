# 모든 비밀번호 조합을 입렵된 조건에 모두 만족하는지 비교 후 맞으면 +1

from itertools import combinations

def solution(n, q, ans):
    answer = 0
    all_possible_code = combinations(range(1, n + 1), 5)
    question_set = [set(query) for query in q]

    for code in all_possible_code:
        code_set = set(code)
        is_success = True

        for i in range(len(q)):
            if len(code_set & question_set[i]) != ans[i]:
                is_success = False
                break

        if is_success:
            answer += 1

    return answer


print(
    solution(
        10,
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [3, 7, 8, 9, 10],
            [2, 5, 7, 9, 10],
            [3, 4, 5, 6, 7],
        ],
        [2, 3, 4, 3, 3],
    )
)
