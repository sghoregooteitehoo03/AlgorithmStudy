# 플로이드워셜로 접근
# 상대방을 이겼는지 졌는지를 판별(a가 k를 이기고 k가 b를 이기면 a는 b를 무조건 이기는것 반대로 b는 지는것)
# 승패의 수가 n - 1이라면 answer + 1

def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]    
    
    for win, lose in results:
        graph[win][lose] = 1
        graph[lose][win] = -1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
                    graph[b][a] = -1

    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if graph[i][j] != 0:
                count += 1
        
        if count == n - 1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))