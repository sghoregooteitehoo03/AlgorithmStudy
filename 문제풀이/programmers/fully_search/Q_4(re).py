# yellow가 짝수인지 아닌지를 판별
# 홀수면 1자로 배치 짝수면 가로가 세로보다 작지 않을정도로 2를 나누어서 계속 확인

# 0 0 0 0 0 0
# 0 1 1 1 1 0
# 0 0 0 0 0 0

# 0 0 0 0 0 0
# 0 1 1 1 1 0
# 0 1 1 1 1 0
# 0 0 0 0 0 0

# 0 0 0 0 0 0
# 0 1 1 1 1 0
# 0 1 1 1 1 0
# 0 0 0 0 0 0

def solution(brown, yellow):
    answer = []

    if yellow % 2 != 0:
        return [yellow + 2, 3]
    if yellow == 2:
        return [4, 3]
    
    # 1자로 배치할 경우
    brown_value = (yellow * 2) + 6
    if brown == brown_value:
        return [yellow + 2, 3]
    
    half_yellow = yellow // 2
    while half_yellow > 1:
        brown_value = (half_yellow * 2) + 6
        


    return answer

print(solution(12, 3))