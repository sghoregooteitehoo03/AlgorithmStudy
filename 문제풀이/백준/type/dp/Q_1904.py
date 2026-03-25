# 1 = 1
# 2 = 00, 11 2
# 3 = 111, 001, 100
# 4 = 0000, 0011, 1100, 1001, 1111 5

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    previous = 1
    current = 2
    answer = 0
    for i in range(3, n + 1):
        answer = (current + previous) % 15746
        
        previous = current
        current = answer
    print(answer)