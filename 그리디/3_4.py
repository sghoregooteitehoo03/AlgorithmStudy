n, k = map(int, input().split())
result = 0
   
while True:
    if n == 1:
        break

    if n % k == 0:
        n /= k
        result += 1
    else:
        if n > k:
            count = (n % k)

            n -= count
            result += count
        else:
            result += n - 1
            n = 1

print(int(result))

# 25, 5
# 25, 3