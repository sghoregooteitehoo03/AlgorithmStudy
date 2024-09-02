def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        price = prices[i]
        
        stack.append((price, i))



    return answer