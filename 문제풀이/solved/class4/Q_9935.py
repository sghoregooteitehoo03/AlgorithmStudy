import sys
input = sys.stdin.readline

s_arr = input().strip()
bomb_str = input().strip()

del_pos = []
stack = []
result = []
    
for i in range(len(s_arr)):
    if len(stack) != 0 and s_arr[i] == bomb_str[stack[-1][1] + 1]:
        if bomb_str[stack[-1][1] + 1] == bomb_str[-1]:
            del stack[len(stack) - (len(bomb_str) - 1):len(stack)]
        else:
            stack.append((s_arr[i], stack[-1][1] + 1))
    elif s_arr[i] == bomb_str[0]:
        stack.append((bomb_str[0], 0))
    elif len(stack) != 0 and s_arr[i] != bomb_str[stack[-1][1] + 1]:
        result.extend(stack)
        result.append((s_arr[i], 0))
        stack.clear()
    else:
        result.append((s_arr[i], 0))

if len(result) == 0:
    print("FRULA")
else:
    data = ''
    for s in result:
        data += s[0]
    print(data)