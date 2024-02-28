import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] #청므엔 모든 수가 소수인 것으로 초기화(0과 1은 제외)

for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: #i가 소수인 경우(남은 수인 경우)
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end= ' ')