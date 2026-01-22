n = int(input())
group = list(map(int, input().split()))
result = 0
i = 0

group.sort(reverse=True)
while i < len(group):
    i += group[i]
    print(i)

    if i <= len(group):
        result += 1
print(result)

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)

# result = 0
# left = arr[0]
# for i in range(len(arr)):
#     left -= 1
    
#     if left == 0:
#         result += 1
        
#         if i < len(arr) - 1:
#             left = arr[i + 1]

# print(result)

# n = int(input())
# traveler = list(map(int, input().split()))
# result = 0
# i = 0
# traveler.sort(reverse=True)

# while i < n:
#     cost = traveler[i]
#     rangeVal = (i + cost)

#     if(rangeVal) <= n:
#         group = traveler[i:rangeVal]

#         if len(group) == cost:
#             result += 1
#             i = (rangeVal - 1)
    
#     i += 1

# print(result)