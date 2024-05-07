import sys
input = sys.stdin.readline

dp = [[-1] * 2001 for _ in range(2001)]

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

def is_same(s, e):
    if dp[s] == 1:
        return 1
    elif dp[s] == 0:
        return 0
    
    if s == e:
        dp[1][s] = 1
        return 1
    elif s + 1 == e:
        cal = int(arr[s] == arr[e])
        dp[2][s] = cal
        return cal
    else:
        diff = e - s
        dp[diff][s] = int(bool(int(arr[s] == arr[e])) and bool(is_same(s + 1, e - 1)))
        return dp[diff][s]

for i in range(m):
    s, e = map(int, input().split())
    print(is_same(s - 1, e - 1))