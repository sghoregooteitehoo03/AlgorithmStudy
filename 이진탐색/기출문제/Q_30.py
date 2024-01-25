# https://school.programmers.co.kr/learn/courses/30/lessons/60060
from bisect import bisect_left, bisect_right

def binary_search(word):
    is_left_start = False
    left = 0
    right = len(word) - 1

    if word[0] == '?' and word[-1] == '?':
        return (left, right)
    elif word[0] == '?':
        is_left_start = True

    while(left <= right):
        mid = (left + right) // 2
        
        if word[mid] == '?':
            if is_left_start:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if is_left_start:
                right = mid - 1
            else:
                left = mid + 1

    if is_left_start:
        return (0, left - 1)
    else:
        return (right + 1, len(word) - 1)


def solution(words, queries):
    answer = [0] * len(queries)
    
    for q in queries:
        left_index, right_index = binary_search(q)
        print(q)
            
        if(left_index > 0):
            slice_value = q[0:left_index]
            
            for word in words:
                if slice_value == word[0:left_index]:
                    answer.
                    
        else:
            slice_value = q[right_index + 1:len(q)]
            print(slice_value)
            print()

    return answer

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"])
