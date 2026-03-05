# 큐에 두 수를 더했을때와 뺏을때의 경우의 수를 넣음
# 모든 연산이 끝났을 때 target값과 같은게 몇개있는지 카운트
from collections import deque

def bfs(numbers, target):
    queue = deque([(-numbers[0] + numbers[1], 1), (numbers[0] + numbers[1], 1), (-numbers[0] - numbers[1], 1), (numbers[0] - numbers[1], 1)])
    count = 0
    
    while queue:
        sum_value, index = deque.popleft(queue)

        if index + 1 < len(numbers):
            queue.append((sum_value + numbers[index + 1], index + 1))
            queue.append((sum_value - numbers[index + 1], index + 1))
        else:
            if sum_value == target:
                count += 1
    
    return count

def solution(numbers, target):
    return bfs(numbers, target)

# print(solution([1, 1, 1, 1, 1], 3))
print(solution([5, 2, 8], 1))
# print(solution([4, 1, 2, 1], 4))