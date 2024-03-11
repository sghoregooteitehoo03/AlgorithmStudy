str_data = []
result = []

while True:
    s = input()
    if s == '.':
        break
    
    str_data.append(s)

for s in str_data:
    stack = []
    is_break = False

    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                is_break = True
                break

            if stack[-1] != '(':
                is_break = True
                break
            else:
                stack.pop()
        elif c == ']':
            if len(stack) == 0:
                is_break = True
                break

            if stack[-1] != '[':
                is_break = True
                break
            else:
                stack.pop()

    result.append(len(stack) != 0 or is_break)

for b in result:
    if not b:
        print("yes")
    else:
        print("no")