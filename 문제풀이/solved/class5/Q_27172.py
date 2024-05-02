import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max_value = max(arr)

table = [(0, False)] * (1000001)

for data in arr:
    table[data] = (0, True)

for i in range(1, (1000000 // 2) + 1):
    if table[i][1]:
        j = 2
        while i * j <= max_value:
            if table[i * j][1]:
                table[i] = (table[i][0] + 1, True)
                table[i * j] = (table[i * j][0] - 1, True)
            j += 1

for data in arr:
    print(table[data][0], end=' ')
print()