# https://www.acmicpc.net/problem/10825
n = int(input())
arr = []

for i in range(n):
    name, k, e, m = input().split()
    arr.append((name, int(k), int(e), int(m)))

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name in arr:
    print(name[0])