# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    n = len(s)
    answer = len(s)

    step = 1
    i = 0
    prevalue = ""
    comp_str = ""
    count = 0

    while step <= (n // 2):
        if i + step <= n:
            current = s[i : i + step]

            if prevalue != "" and current != prevalue:
                if 1 < count:
                    comp_str += str(count) + prevalue
                else:
                    comp_str += prevalue
                count = 0

            prevalue = current
            count += 1
            i += step
        else:
            if prevalue != "":
                if 1 < count:
                    comp_str += str(count) + prevalue + s[i::]
                else:
                    comp_str += prevalue + s[i::]
                count = 0

            answer = min(answer, len(comp_str))
            step += 1
            i = 0
            prevalue = ""
            comp_str = ""

    return answer

# def solution(s):
#     if len(s) == 1:
#         return 1
    
#     half = len(s) // 2
#     result = 1e9
#     for i in range(1, half + 1):
#         comp_str = ""
#         comp_count = 1
#         previous = s[0:i]
#         current_index = i
        
#         while current_index < len(s):
#             currenet = s[current_index:i + current_index]
#             if previous == currenet:
#                 comp_count += 1
#             else:
#                 if comp_count > 1:
#                     comp_str += (str(comp_count) + previous)
#                     comp_count = 1
#                 else:
#                     comp_str += previous
                
#             previous = currenet
#             current_index += i
                
#         if comp_count > 1:
#             comp_str += (str(comp_count) + previous)
#             comp_count = 1
#         else:
#             comp_str += previous
            
#         result = min(result, len(comp_str))
#     return result


# def solution(str):
#     len_array = []
#     strLen = len(str)
#     half = strLen // 2
#     increase = 1

#     while increase <= half:
#         strArray = []
#         latestStr = ""
#         index = 0
#         count = 1

#         for i in range(0, strLen, increase):
#             index = i
#             s = str[i:i+increase]
#             if latestStr == s:
#                 count += 1
#             else:
#                 if count == 1:
#                     strArray.append(latestStr)
#                 else:
#                     strArray.append(count.__str__() + latestStr)

#                 count = 1
#                 latestStr = s

#         if count == 1:
#             strArray.append(latestStr)
#         else:
#             strArray.append(count.__str__() + latestStr)

#         strArray.append(str[index + increase:strLen])
#         len_array.append(len("".join(strArray)))

#         increase += 1

#     if len(len_array) == 0:
#         return 1
#     else:
#         return min(len_array)

# print(solution("a"))


# aabbaccc 2a2ba3c
# ababcdcdababcdcd 2ababcdcd
# abcabcdede 2abcdede
# abcabcabcabcdededededede 2abcabc2dedede