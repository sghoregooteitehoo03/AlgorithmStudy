# DP문제
# 두 도둑이 n, m 이상의 흔적을 남기지 않으면서 모든 물건을 훔치게 해야함
# 단 A도둑이 최소로 흔적을 남겨야함
INF = 1e9

def solution(info, n, m):
    dp = [INF] * n
    dp[0] = 0  # 초기 상태: 훔친 물건이 없으므로 둘 다 흔적 0

    for trace_a, trace_b in info:
        next_dp = [INF] * n

        for a in range(n):
            if dp[a] == INF:
                continue

            if a + trace_a < n:
                next_dp[a + trace_a] = min(next_dp[a + trace_a], dp[a])

            if dp[a] + trace_b < m:
                next_dp[a] = min(next_dp[a], dp[a] + trace_b)
        
        dp = next_dp

    for a in range(n):
        if dp[a] != INF:
            return a

    return -1

print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))