str = input()
result = 0

for s in str:
    n = int(s)
    
    if result == 0 or n == 1:
        result += n
    else:
        result *= n

print(result)