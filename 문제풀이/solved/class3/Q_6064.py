import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())

    i = x
    j = x
    result = x
    is_found = False

    for _ in range((m * n) // 2):
        if i == x and j == y:
            is_found = True
            break

        j += m
        result += m

        while j >= n:
            j -= n

    if is_found:
        print(result)
    else:
        print(-1)
