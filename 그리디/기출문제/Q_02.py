s = input()

result = int(s[0])
for i in range(1, len(s)):
    current = int(s[i])
    
    if current <= 1 or result <= 1:
        result += current
    else:
        result *= current
        
print(result)