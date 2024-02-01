n = int(input())
i = 0
dict = {1: 1}

while(len(dict.keys()) <= n):
    key = list(dict.keys())[i]
    dict[key * 2] = key * 2
    dict[key * 3] = key * 3
    dict[key * 5] = key * 5
    
    i += 1

result = list(dict.keys())
result.sort()
print(result[n - 1])