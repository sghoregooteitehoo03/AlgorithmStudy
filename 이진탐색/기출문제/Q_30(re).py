# https://school.programmers.co.kr/learn/courses/30/lessons/60060
from bisect import bisect_left, bisect_right

def binary_search(arr, left_value, right_value):
    l_index = bisect_left(arr, left_value)
    r_index = bisect_right(arr, right_value)

    return r_index - l_index

def solution(words, queries):
    answer = []
    divide_len_word = [[] for _ in range(10001)]
    reverse_len_word = [[] for _ in range(10001)]

    for word in words:
        divide_len_word[len(word)].append(word)
        reverse_len_word[len(word)].append(word[::-1])

    for i in range(10001):
        divide_len_word[i].sort()
        reverse_len_word[i].sort()

    for q in queries:
        res = 0
        if q[0] != '?':
            res = binary_search(divide_len_word[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = binary_search(reverse_len_word[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))

        answer.append(res)
                    
    return answer

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?", "?????"])