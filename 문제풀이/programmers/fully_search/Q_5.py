# 모든 경우의 수를 생성
# 그 경우의 수에서 최대로 던전을 돌 수 있는 수를 리턴

from itertools import permutations

def solution(k, dungeons):
    answer = -1

    for i in range(1, len(dungeons) + 1):
        for roots in permutations(dungeons, i):
            point = k
            count = 0
            for root in roots:
                if point >= root[0]:
                    count += 1
                    point -= root[1]
                
                if point == 0:
                    break
            
            answer = max(answer, count)

    return answer

print(solution(80, [[80,20],[50,40],[30,10], [80,20],[50,40],[30,10], [80,20],[50,40]]))