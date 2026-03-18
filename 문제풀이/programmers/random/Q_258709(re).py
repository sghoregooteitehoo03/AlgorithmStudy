# 조합 문제
# 선택한 주사위들과 선택받지 못한 주사위들의 합을 구한 뒤 이긴수를 계산
# 가장 이긴 횟수가 많은 주사위 조합을 찾고 그 조합을 반환함

from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    dice_indices = set(range(n))

    max_wins = 0
    best_dice_combo = []

    for a_combo in combinations(range(n), n // 2):
        b_combo = tuple(dice_indices - set(a_combo))

        a_sums = [sum(p) for p in product(*[dice[i] for i in a_combo])]
        b_sums = [sum(p) for p in product(*[dice[i] for i in b_combo])]

        b_sums.sort()
        wins = 0

        for a_sum in a_sums:
            wins += bisect_left(b_sums, a_sum)

        if max_wins < wins:
            max_wins = wins
            best_dice_combo = a_combo

    return [x + 1 for x in best_dice_combo]


print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))