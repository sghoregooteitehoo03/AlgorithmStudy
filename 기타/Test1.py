import math

m, n = map(int, input().split())
array = [True] * (1000001)
array[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    
    if array[i] == True: #i가 소수인 경우(남은 수인 경우)
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(m, n + 1):
    if i == 1:
        continue

    if array[i] == True:
        print(i)