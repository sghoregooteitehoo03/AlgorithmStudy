def solution(priorities, location):
    answer = 0
    stack = []

    for i in range(len(priorities)):
        priorities[i] = (priorities[i], i)

    i = 0
    while True:
        if len(priorities) == 0:
            break
        
        max_value = max(priorities)[0]
        priority, index = priorities[i]
            
        if priority == max_value:
            stack.append(index)
            priorities.pop(i)
            
            i -= 1

        i += 1
        if i >= len(priorities):
            i = 0

    for i in range(len(stack)):
        index = stack[i]
        if index == location:
            answer = i + 1
            break

    return answer

# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([1, 1], 0))