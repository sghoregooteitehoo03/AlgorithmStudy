n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0
count = m

numbers.sort(reverse=True)
print(numbers)
while count > 0:
    if count >= k:
        result += numbers[0] * k
        count -= k
    else:
        result += numbers[0] * count
        count = 0

    if count > 0:
        result += numbers[1]
        count -= 1

print(result)

# 답지(최적화)
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n - 1]
# second = data[n - 2]

# count = int(m / (k + 1)) * k
# count += m % (k + 1)

# result = 0
# result += (count) * first
# result += (m - count) * second

# print(result)
