import sys
input = sys.stdin.readline
dp = [0] * 100000
pos = [0, 0]

arr = list(map(int, input().split()))
arr.pop(-1)

if len(arr) == 0:
    print(0)
elif len(arr) < 2:
    print(2)
else:
    pos[0] = arr[0]
    dp[0] = 2

    for i in range(1, len(arr)):
        number = arr[i]
        min_length = 4
        
        if number - pos[0] == 0 or number - pos[0] == 0:
            min_length = 1
        else:
            if pos[1] == 0:
                dp[i] = dp[i - 1] + 2
                continue
            
            if abs(number - pos[0]) == 2:
                min_length = 4
            else:
                min_length = 3

            if abs(number - pos[1]) == 2:
                min_length = 4
            else:
                min_length = 3

        dp[i] = dp[i - 1] + min_length
    
    result = max(dp)
    print(result)

# 2 1 3 2 3 0