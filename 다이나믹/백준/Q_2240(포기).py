import sys
input = sys.stdin.readline

t, w = map(int, input().split())
arr = []
dp = []
tc1 = 0
tc2 = 0
result = 0

for i in range(t):
    arr.append(int(input()))

if arr[0] == 1:
    tc1 = (1, 1, 0)
    tc2 = (0, 2, 1)
    result = 1
else:
    tc1 = (0, 1, 0)
    tc2 = (0, 2, 1)

for i in range(1, t - 1):
    if i == 1:
        if arr[i] == 1:
            dp.append((tc1[0] + 1, 1, 0))
        else:
            dp.append((tc2[0] + 1, 1, 0))
