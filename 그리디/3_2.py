N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

result = 0
count = 0

while True:
    if count >= M:
        break

    count += K + 1
    if (M - count) < 0:
        divide = M - (count - (K+1))
        count += divide

        result += numbers[0] * divide
    else:
        divide = K

        result += numbers[0] * divide
        result += numbers[1]

print(result)

# 답지
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