# 각 돌의 거리를 mid(거리의 최솟값)로 선정
# mid보다 작은 돌은 카운트 그게 아니면 빼버림
# 돌을 n보다 많이 뽑으면 거리를 더 줄임 그게 아니면 거리를 더 넓힘

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left = 0
    right = distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        remove_count = 0
        current_pos = 0

        for rock in rocks:
            diff = rock - current_pos

            if diff < mid:
                remove_count += 1
            else:
                current_pos = rock

        if remove_count > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))