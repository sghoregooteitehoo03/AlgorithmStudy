# 배열의 길이 n -1 지점에서 더했을때 큰 값을 선택
# 마지막까지 선택해서 마지막값을 출력

def solution(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            max_value = max(triangle[i + 1][j], triangle[i + 1][j + 1])
            triangle[i][j] = triangle[i][j] + max_value

    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))