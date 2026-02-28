# 가로, 세로의 제일 높은 값을 추출
# 가로와 세로의 어떤 값 중 선택해 이 제일 높은 값이 그 값에 포함될 수 있는지를 비교

def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        w, h = max(w, h), min(w, h)
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_w * max_h

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))