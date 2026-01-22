# https://www.acmicpc.net/problem/1439
import sys
input = sys.stdin.readline

s = input().strip()
zero_count = 0
one_count = 0
latest_value = -1

for c in s:
    n = int(c)
    if latest_value != n:
        if n == 0:
            zero_count += 1
            latest_value = 0
        else:
            one_count += 1
            latest_value = 1

print(min(one_count, zero_count))

# import sys
# input = sys.stdin.readline
# s = input()

# one_continuous = 0
# zero_continuous = 0

# previous = s[0]
# for i in range(1, len(s)):
#     current = s[i]
    
#     if previous != current:
#         if previous == '1':
#             one_continuous += 1
#         else:
#             zero_continuous += 1
#     previous = current
            
# print(min(one_continuous, zero_continuous))

# str = input()
# latest = -1
# isFirst = False
# result = [0, 0]

# for s in str: 
#     n = int(s)
    
#     if latest != n:
#         latest = n
#         isFirst = True

#     if isFirst:
#         isFirst = False
#         result[latest] += 1

# print(min(result))