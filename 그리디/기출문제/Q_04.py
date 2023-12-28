n = int(input())
moneyList = list(map(int, input().split()))
result = 0

moneyList.sort(reverse=True)
while True:
    result += 1
    calValue = result
    
    for money in moneyList:
        if calValue >= money:
            calValue -= money

        if calValue == 0:
            break
    
    if calValue != 0:
        break

print(result)