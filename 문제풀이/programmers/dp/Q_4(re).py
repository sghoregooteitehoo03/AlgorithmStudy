# 구간 dp

def solution(arr):
    # 1. 숫자와 연산자를 분리합니다.
    nums = [int(x) for x in arr[0::2]]  # [1, 3, 5, 8]
    ops = arr[1::2]  # ['-', '+', '-']
    n = len(nums)

    # 2. DP 테이블 초기화 (최댓값은 아주 작은 수로, 최솟값은 아주 큰 수로)
    max_dp = [[-float("inf")] * n for _ in range(n)]
    min_dp = [[float("inf")] * n for _ in range(n)]

    # 3. 길이가 1인 구간 초기화 (자기 자신)
    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]

    # 4. 구간의 길이(step)를 1칸에서 n-1칸까지 점차 늘려갑니다.
    for step in range(1, n):
        # i는 구간의 시작점, j는 구간의 끝점
        for i in range(n - step):
            j = i + step

            # i부터 j 사이의 연산자 k를 기준으로 식을 두 덩어리로 쪼갭니다.
            for k in range(i, j):
                if ops[k] == "+":
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:  # '-' 인 경우 (빼기의 마법 발동!)
                    # 최댓값 = 기존값 vs (앞단 최대 - 뒷단 최소)
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    # 최솟값 = 기존값 vs (앞단 최소 - 뒷단 최대)
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])

    # 처음 숫자(0)부터 마지막 숫자(n-1)까지 연산한 최댓값을 반환
    return max_dp[0][n - 1]


solution(["1", "-", "3", "+", "5", "-", "8"])
