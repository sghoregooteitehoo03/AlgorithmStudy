# https://school.programmers.co.kr/learn/courses/30/lessons/60058
from collections import deque

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.
def fix_str(w):
    if w == "":
        return ""

    s = ""
    u, v = divide_str(w)
    if check_str(u):
        return u + fix_str(v)
    else:
        s = "(" + fix_str(v) + ")"
        u = u[1:]
        u = u[:-1]
        u_list = list(u)
        for i in range(len(u_list)):
            if u_list[i] == '(':
                u_list[i] = ')'
            else:
                u_list[i] = '('
        u = "".join(u_list)
        return s + u

def check_str(u):
    stack = [u[0]]
    previous_str = u[0]
    for i in range(1, len(u)):
        current_str = u[i]

        if previous_str == "(" and current_str == ")":
            stack.pop()
            if len(stack) != 0:
                previous_str = stack[-1]
            else:
                previous_str = ""
        else:
            stack.append(current_str)
            previous_str = current_str    

    return len(stack) == 0


def divide_str(w):
    left_count = 0
    right_count = 0

    for i in range(len(w)):
        if w[i] == "(":
            left_count += 1
        elif w[i] == ")":
            right_count += 1

        if left_count == right_count:
            break

    u = w[0 : i + 1]
    v = w[i + 1:]
    return (u, v)


def solution(p):
    return fix_str(p)

# def check_right(w):
#     q = deque(w[0])
    
#     for i in range(1, len(w)):
#         previous = q.popleft()
        
#         if previous == '(' and w[i] == ')':
#             continue
        
#         q.append(previous)
#         q.append(w[i])

#     return q.__len__() == 0

# def solution(p):
#     if p == '':
#         return ''

#     u = ''
#     v = ''
#     answer = ''
#     stack1 = 0
#     stack2 = 0
#     for i in range(len(p)):
#         if p[i] == '(':
#             stack1 += 1
#         else:
#             stack2 += 1

#         if stack1 == stack2:
#             u = p[:i + 1]
#             v = p[i + 1:len(p)]
#             break

#     if check_right(u):
#         answer = u + solution(v)
#         return answer
#     else:
#         answer = '('
#         answer += solution(v)
#         answer += ')'
        
#         u = u[1:len(u) - 1]
#         reverse = ''
#         for c in u:
#             if c == '(':
#                 reverse += ')'
#             else:
#                 reverse += '('
        
#         return answer + reverse