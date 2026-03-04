# 구간 스케줄링

# [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
# 이중 포문 사용
# 한 차를 기준으로 그 범위에 들어가는 모든 차를 계산
# 그걸 카운트

def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])

    camera = -30001
    for route in routes:
        start = route[0]
        end = route[1]

        if start > camera:
            answer += 1
            camera = end

    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])