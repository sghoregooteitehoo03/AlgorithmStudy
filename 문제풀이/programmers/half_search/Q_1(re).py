# 우리가 임의로 X분이라는 시간을 던져줄 테니', 그 X분 동안 니들(심사관들)이 총 몇 명을 심사할 수 있는지 계산해 봐! 그게 $N$명보다 많아? 적어?"

def solution(n, times):
    left = 1
    right = max(times) * n
    
    answer = right
    while left <= right:
        mid = (left + right) // 2

        people_count = 0
        for time in times:
            people_count += mid // time

            if people_count >= n:
                break

        if people_count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

print(solution(6, [7, 10]))