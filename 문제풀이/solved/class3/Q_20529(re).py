import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    ans = 999999
    n = int(input())
    a = list(input().split())
    if n > 32:
        print(0)
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmp = 0
                    if i == j or j == k or i == k:
                        continue
                    for x in range(4):
                        if a[i][x] != a [j][x]: tmp += 1
                        if a[j][x] != a [k][x]: tmp += 1
                        if a[i][x] != a [k][x]: tmp += 1
                    ans = min(tmp, ans)

        print(ans)