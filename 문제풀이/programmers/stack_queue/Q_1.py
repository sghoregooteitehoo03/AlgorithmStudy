def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        number = arr[i]
        if answer[-1] != number:
            answer.append(number)

    return answer

print(solution([1,1,3,3,0,1,1]))