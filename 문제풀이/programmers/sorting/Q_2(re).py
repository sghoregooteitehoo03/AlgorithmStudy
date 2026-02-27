# 모든 경우의 수를 생성
# 그걸 문자열로 서로 붙임
# 가장 큰 수를 배출
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = "".join(numbers)

    if answer[0] == "0":
        return "0"
    return answer


solution([6, 10, 2])
# solution([3, 30, 34, 5, 9])
