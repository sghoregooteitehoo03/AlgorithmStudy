import sys
input = sys.stdin.readline

code = input().rstrip()
dp = [0] * len(code)

for i in range(len(code) - 1, -1, -1):
    if i == len(code) - 1:
        if int(code[i]) > 0:
            dp[i] = 1
    else:
        if int(code[i]) > 0:
            dp[i] = dp[i + 1]

            cal = int(code[i] + code[i + 1])
            if cal < 27 and cal >=10:
                if i + 2 < len(code):
                    dp[i] += dp[i + 2]
                else:
                    dp[i] += 1

if dp[0] == 0:
    print(0)
else:
    print(dp[0] % 1000000)