# 무게수를 오름차순 정렬
# 가장 무거운 사람과 가장 가벼운 사람을 함께 태울 수 있는지 확인
# 가능하면 가벼운 사람을 다음으로 넘김
# 불가능하면 무거운 사람을 내보냄

def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        answer += 1

    return answer


print(solution([10, 20, 30, 40, 50], 80))  # 2
print(solution([70, 50, 80, 50], 100))
print(solution([70, 20, 80, 50], 150))
print(solution([70, 80, 50], 100))
# 50 50 70 40 80
