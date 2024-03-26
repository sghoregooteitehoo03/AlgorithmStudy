import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
result = 0

find_value = ''
for i in range(n):
    find_value += 'I'
    find_value += 'O'
find_value += 'I'

i = len(find_value)
while i < len(s):
    if find_value == s[i - len(find_value):i]:
        i += 2
        result += 1
        continue

    i += 1

print(result)