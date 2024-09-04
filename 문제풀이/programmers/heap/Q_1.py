import heapq

def solution(scoville, K):
    answer = 0
    q = []
    for i in range(len(scoville)):
        number = scoville[i]
        heapq.heappush(q, number)

    while True:
        number1 = heapq.heappop(q)

        if number1 < K:
            if len(q) == 0:
                answer = -1
                break
            number2 = heapq.heappop(q)

            mix_value = number1 + (number2 * 2)
            heapq.heappush(q, mix_value)
            answer += 1
        else:
            break

    return answer


solution([1, 2, 3, 9, 10, 12], 7)
