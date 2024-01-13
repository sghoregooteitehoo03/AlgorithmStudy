# https://school.programmers.co.kr/learn/courses/30/lessons/60058
from collections import deque

def check_right(w):
    q = deque(w[0])
    
    for i in range(1, len(w)):
        previous = q.popleft()
        
        if previous == '(' and w[i] == ')':
            continue
        
        q.append(previous)
        q.append(w[i])

    return q.__len__() == 0

def solution(p):
    if p == '':
        return ''

    u = ''
    v = ''
    answer = ''
    stack1 = 0
    stack2 = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack1 += 1
        else:
            stack2 += 1

        if stack1 == stack2:
            u = p[:i + 1]
            v = p[i + 1:len(p)]
            break

    if check_right(u):
        answer = u + solution(v)
        return answer
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        u = u[1:len(u) - 1]
        reverse = ''
        for c in u:
            if c == '(':
                reverse += ')'
            else:
                reverse += '('
        
        return answer + reverse

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))