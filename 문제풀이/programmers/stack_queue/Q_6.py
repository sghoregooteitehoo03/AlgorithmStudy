def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        price = prices[i]
        count = 0

        for j in range(i + 1, len(prices)):
            other_price = prices[j]
            count += 1

            if price > other_price:
                break
            
        answer[i] = count

    return answer

# solution([1, 2, 3, 2, 3])
# solution([1, 2, 3, 2, 3, 1])