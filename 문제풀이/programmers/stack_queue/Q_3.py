def solution(s):
    stack = []

    for c in s:
        if c == '(':
            stack.append("(")
        else:
            if len(stack) != 0:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                return False

    return len(stack) == 0

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
