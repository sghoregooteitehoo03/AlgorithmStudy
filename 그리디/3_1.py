n = int(input())
counterMoney = [500, 100, 50, 10]
count = 0

for money in counterMoney:
    divide = n // money
    n -= money * divide

    count += divide

print(count)

# 답지
# n = input()
# count = 0

# coin_types = [500, 100, 50, 10]
# for coin in coin_types:
#     count += n // coin
#     n %= coin

# print(count)