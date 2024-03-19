import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    command = input()
    n = int(input())
    str_data = input()
    q = deque(eval(str_data))
    
    is_error = False
    is_reverse = False
    
    if n != len(q):
        is_error = True

    if not is_error:
        for c in command:
            if c == 'R':
                is_reverse = not is_reverse
            elif c == 'D':
                if len(q) != 0:
                    if is_reverse:
                        q.pop()
                    else:
                        q.popleft()
                else:
                    is_error = True
                    break

    if is_error:
        print('error')
    else:
        if len(q) == 0:
            print('[]')
        else:
            q = list(q)
            if is_reverse:
                print("[" + ",".join(str(x) for x in q[::-1]) + "]")
            else:
                print("[" + ",".join(str(x) for x in q) + "]")
