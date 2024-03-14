from collections import deque
import sys
input = sys.stdin.readline

def cal_D(x):
    n = int(x)
    if n * 2 > 9999:
        return str(((n * 2) % 10000)).zfill(4)
    else:
        return str(n * 2).zfill(4)

def cal_S(x):
    n = int(x)
    if n == 0:
        return '9999'
    else:
        return str(n - 1).zfill(4)

def cal_L(x):
    a, b, c, d = x
    
    return b + c + d + a

def cal_R(x):
    a, b, c, d = x
    
    return d + a + b + c

t = int(input())

for i in range(t):
    a, b = input().split()
    result = ''
    visited = [False] * 10000
    
    formatted_a = a.zfill(4)
    formatted_b = b.zfill(4)

    q = deque([(cal_D(formatted_a), 'D'), (cal_S(formatted_a), 'S'), (cal_L(formatted_a), 'L'), (cal_R(formatted_a), 'R')])
    visited[int(cal_D(formatted_a))] = True
    visited[int(cal_S(formatted_a))] = True
    visited[int(cal_L(formatted_a))] = True
    visited[int(cal_R(formatted_a))] = True
    
    while(q):
        cal_a, sequence = q.popleft()

        if cal_a == formatted_b:
            result = sequence
            break

        if not visited[int(cal_D(cal_a))]:
            visited[int(cal_D(cal_a))] = True
            q.append((cal_D(cal_a), sequence + 'D'))
        
        if not visited[int(cal_S(cal_a))]:
            visited[int(cal_S(cal_a))] = True
            q.append((cal_S(cal_a), sequence + 'S'))
        
        if not visited[int(cal_L(cal_a))]:
            visited[int(cal_L(cal_a))] = True
            q.append((cal_L(cal_a), sequence + 'L'))

        if not visited[int(cal_R(cal_a))]:
            visited[int(cal_R(cal_a))] = True
            q.append((cal_R(cal_a), sequence + 'R'))

    print(result)
