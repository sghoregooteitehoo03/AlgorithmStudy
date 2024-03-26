import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    history = [False] * 40001

    i = x
    j = x
    
    result = x
    while j > n:
        j -= n
            
    history[j] = True
    is_found = False

    while True:
        if i == x and j == y:
            is_found = True
            break

        j += m
        result += m

        if j < n:
            if history[j]:
                break
        else:
            while j > n:
                j -= n
        
            if history[j]:
                break
        
        history[j] = True

    if is_found:
        print(result)
    else:
        print(-1)
