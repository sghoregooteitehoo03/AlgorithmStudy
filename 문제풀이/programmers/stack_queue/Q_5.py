from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0

    while truck_weights:
        answer += 1
        current_weight = current_weight - bridge.popleft()

        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    return answer + bridge_length

print(solution(2, 10, [7,4,5,6]))
# print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))