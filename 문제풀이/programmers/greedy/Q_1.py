# 기본 count = n - len(lost)로 시작
# lost 숫자를 기본으로 여러벌 체육복의 내용을 비교(둘의 차이가 1보다 크거나 작으면 카운트 그게 아니면 스킵)
# 카운트가 n이랑 같으면 스탑

def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()

    for lost_n in lost:
        for i in range(len(reserve)):
            reserve_n = reserve[i]

            if abs(reserve_n - lost_n) == 1 and reserve_n not in lost:
                reserve.pop(i)
                answer += 1
                break
            elif lost_n == reserve_n:
                reserve.pop(i)
                answer += 1
                break

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(5, [2, 4], [2]))
print(solution(3, [3], [1]))
