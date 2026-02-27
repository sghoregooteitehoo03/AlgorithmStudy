# 2중 for 문으로 어느 논문의 인용횟수를 카운트
# 그 카운트를 기준으로 인용된 논문이 그 이상이면서 인용되지 않은 논문이 그 카운트 값 이하면 그 값이 정답

def solution(citations):
    n = len(citations)
    citations.sort(reverse = True)
    answer = 0

    for i in range(max(citations)):
        count = 0

        for j in range(len(citations)):
            if i <= citations[j]:
                count += 1

        if i <= count and i >= (n - count):
            answer = i
        else:
            break
    
    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([5, 6, 7, 8]))