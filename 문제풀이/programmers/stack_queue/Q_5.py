def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = []

    for truck_weight in truck_weights:
        stack.append(truck_weight)

        if sum(stack) > weight:
            stack.pop(-1)
            answer += len(stack) * bridge_length

            stack.clear()
            stack.append(truck_weight)

    answer += len(stack)

    return answer

print(solution(2, 10, [7,4,5,6]))