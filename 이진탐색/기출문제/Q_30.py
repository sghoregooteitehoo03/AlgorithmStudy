# https://school.programmers.co.kr/learn/courses/30/lessons/60060
from bisect import bisect_left, bisect_right

def search(words, left, right):
    left_index = bisect_left(words, left)
    right_index = bisect_right(words, right)

    return right_index - left_index

def solution(words, queries):
    answer = []
    sorted_words = [[] for _ in range(10001)]
    reverse_words = [[] for _ in range(10001)]

    for word in words:
        sorted_words[len(word)].append(word)
        reverse_words[len(word)].append(word[::-1])

    for i in range(10001):
        sorted_words[i].sort()
        reverse_words[i].sort()

    for query in queries:
        res = 0
        if query[0] != "?":
            res = search(
                sorted_words[len(query)],
                query.replace("?", "a"),
                query.replace("?", "z"),
            )
        else:
            res = search(
                reverse_words[len(query)],
                query[::-1].replace("?", "a"),
                query[::-1].replace("?", "z"),
            )
        answer.append(res)

    return answer

# from bisect import bisect_left, bisect_right

# def binary_search(arr, left_value, right_value):
#     l_index = bisect_left(arr, left_value)
#     r_index = bisect_right(arr, right_value)

#     return r_index - l_index

# def solution(words, queries):
#     answer = []
#     divide_len_word = [[] for _ in range(10001)]
#     reverse_len_word = [[] for _ in range(10001)]

#     for word in words:
#         divide_len_word[len(word)].append(word)
#         reverse_len_word[len(word)].append(word[::-1])

#     for i in range(10001):
#         divide_len_word[i].sort()
#         reverse_len_word[i].sort()

#     for q in queries:
#         res = 0
#         if q[0] != '?':
#             res = binary_search(divide_len_word[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
#         else:
#             res = binary_search(reverse_len_word[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))

#         answer.append(res)
                    
#     return answer

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?", "?????"])