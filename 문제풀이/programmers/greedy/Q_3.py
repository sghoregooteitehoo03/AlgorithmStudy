# stack에 하나씩 담음
# 최근에 담은게 뒤에 숫자보다 작으면 빼버림
# 횟수가 남았으면 남은 수 만큼 잘라냄
# 출력

def solution(number, k):
    stack = []

    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1

        stack.append(n)

    if k > 0:
        stack = stack[:-k]
    return "".join(stack)


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
