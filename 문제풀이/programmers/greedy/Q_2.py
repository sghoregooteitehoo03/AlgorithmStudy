# 문자열을 오름차순으로 찾을때와 내림차순으로 찾을 때 더 이득인 값을 반환
# 문자열을 오른쪽으로 왼쪽으로 이동시킬때 뭐가 더 이득인지 따짐
# 이득인 횟수끼리 더해서 반환

def solution(name):
    count = 0
    
    for s in name:
        count += get_diff(s)

    n = len(name)
    move = n - 1
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == "A":
            next_i += 1

        move = min(move, i * 2 + (n - next_i), (n - next_i) * 2 + i)
    return count + move

def get_diff(s):
    return min(ord(s) - ord("A"), ord("Z") - ord(s) + 1)