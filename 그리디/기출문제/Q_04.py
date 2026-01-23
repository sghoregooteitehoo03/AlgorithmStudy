n = int(input())
coins = list(map(int, input().split()))
coins.sort()
target = 1

for coin in coins:
    if coin <= target:
        target += coin

print(target)

# n = int(input())
# coins = list(map(int, input().split()))

# coins.sort()

# target = 1
# for coin in coins:
#     if target < coin:
#         break
#     target += coin
    
# print(target)

# n = int(input())
# moneyList = list(map(int, input().split()))
# result = 0

# moneyList.sort(reverse=True)
# while True:
#     result += 1
#     calValue = result
    
#     for money in moneyList:
#         if calValue >= money:
#             calValue -= money

#         if calValue == 0:
#             break
    
#     if calValue != 0:
#         break

# print(result)