def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = []
    total = 0
    i = 0

    while i < len(truck_weights):
        truck_weight = truck_weights[i]
        total += truck_weight
        
        if len(stack) == 0 or stack[0][0] == 1:
            stack.append((bridge_length, truck_weight))
        else:
            stack.append((1, truck_weight))

        if total > weight:
            total -= truck_weight
            stack.pop(-1)

            v, w = stack.pop(0)
            answer += v
            total -= w
            continue
        
        i += 1

    print(stack)
    if len(stack

    return answer + 1

# print(solution(2, 10, [7,4,5,6]))
print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))