# a -> z 증가 이후 aa -> ab -> zz 이런 순으로 증가
# 금지된 문자 있으면 그거빼고 증가를 수행
# n 번째 숫자의 문자를 반환

# n이 입력 되었을때 계산이 수행되어야 함

# 문자열 문제
# 26진수 (a = 1, z = 26, aa = 27) ae = 31 af 32 ag 33 ah 34
# bans를 확인해서 n보다 작은 숫자면 카운트 
#  카운트 값을 더해서 그걸 해당하는 문자열로 반환

def solution(n, bans):
    ban_nums = []
    for ban in bans:
        value = 0
        for c in ban:
            value = value * 26 + (ord(c) - ord('a') + 1)
        ban_nums.append(value)

    ban_nums.sort()

    target = n
    for num in ban_nums:
        if num <= target:
            target += 1
        else:
            break
    
    res = []
    while target > 0:
        target -= 1
        res.append(chr(target % 26 + ord('a')))
        target //= 26
    return "".join(reversed(res))

print(solution(30, ["d", "e", "bb", "aa", "ae"]))