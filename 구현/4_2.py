n = int(input())
filterling = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
result = 0

for i in range(n + 1):
    if i in filterling:
        result += 3600
    else:
        result += (60 * len(filterling))
        result += ((60 - len(filterling)) * len(filterling))

print(result)