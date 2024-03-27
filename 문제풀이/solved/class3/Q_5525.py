import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
result = 0
pattern = 0
i = 1

while i < m:
    is_pattern = False
    
    if s[i - 1] == 'I' and s[i] == 'O' and s[i + 1] == 'I':
        pattern += 1
        i += 2

        is_pattern = True
    else:
        pattern = 0
        i += 1

    if pattern == n:
        result += 1

        if is_pattern:
            pattern -= 1

print(result)