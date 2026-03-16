# 이분탐색 적용
# 제일 높은 레벨과 낮은 레벨 사이 중 계산 로직을 통해 최솟값을 찾아서 반환
def solution(diffs, times, limit):
    left = min(diffs)
    right = max(diffs)

    answer = right
    while left <= right:
        mid = (left + right) // 2
        time = 0
        time_prev = 0

        for i in range(len(diffs)):
            diff = diffs[i]
            
            if diff <= mid:
                time += times[i]
                time_prev = times[i]
            else:
                value = (times[i] + time_prev) * (diff - mid) + times[i]
                time += value
                time_prev = times[i]
        
        if time > limit:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer

# print(solution([1, 5, 3], [2, 4, 7], 30))
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))
