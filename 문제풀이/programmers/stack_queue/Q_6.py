import heapq

def solution(prices):
    answer = [0] * len(prices)
    q = []

    for i in range(len(prices)):
        price = prices[i]
        heapq.heappush(q, (price, i))

    min_index = 1e9
    max_index = -1

    while q:
        price, index = heapq.heappop(q)
        
        if min_index == 1e9 and max_index == -1:
            answer[index] = (len(prices) - 1) - index
        else:
            if max_index <= index:
                answer[index] = (len(prices) - 1) - index
            elif min_index < index and index < max_index:
                answer[index] = max_index - index
            elif index <= min_index:
                answer[index] = min_index - index
        
        if max_index < index:
            max_index = index
        if min_index > index:
            min_index = index

    print(answer)
    return answer

# solution([1, 2, 3, 2, 3])
solution([1, 2, 3, 2, 3, 1])