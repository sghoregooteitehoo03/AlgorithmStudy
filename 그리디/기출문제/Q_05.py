import itertools
n, m = map(int, input().split())
arr = list(map(int, input().split()))

comb = itertools.combinations(arr, 2)
count = 0
for x in comb:
    if x[0] != x[1]:
        count += 1
        
print(count)

# n, m = map(int, input().split())
# ballList = list(map(int, input().split()))
# countList = [0] * (m + 1)
# result = 0

# for i in range(n):
#     countList[ballList[i]] += 1

# for i in range(n - 1):
#     ball = ballList[i]
    
#     for j in range(1, m + 1):
#         if ball != j:
#             result += countList[j]
    
#     countList[ball] -= 1

# print(result)