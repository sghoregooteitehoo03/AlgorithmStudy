n, k = map(int, input().split())
money = []
result = 0

for i in range(n):
    money.append(int(input()))

money.sort(reverse=True)
j = 0

while k != 0:
    if k >= money[j]:
        k -= money[j]
        result += 1
    else:
        j += 1

print(result)