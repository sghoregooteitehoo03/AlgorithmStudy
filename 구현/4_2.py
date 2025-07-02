n = int(input())
result = 1575

for i in range(n):
    if (i + 1) == 3 or (i + 1) == 13 or (i + 1) == 23:
        result += 3600
    else:
        result += 1575

print(result)