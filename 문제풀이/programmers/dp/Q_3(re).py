[0, 0, 0, 0, 0]
[0, 1, 1, 1, 1]
[0, 1, 0, 1, 2]
[0, 1, 1, 2, 4]

[0, 1, 2, 3, 4, 5]
[1, 10, 10, 10, 10, 10]
[2, 3, 4, 5, 0, 0]
[3, 0, 0, 0, 0, 8]
[4, 0, 0, 0, 0, 0]
[5, 0, 0, 0, 0, 0]

# 특정위치에서 위에서 왼쪽에서 오는 경로의 수를 카운트

def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == 1:
                continue

            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]

print(solution(4, 3, [[2, 2]]))