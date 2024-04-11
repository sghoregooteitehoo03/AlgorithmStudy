import sys
input = sys.stdin.readline

s_arr = input().rstrip()
bomb_str = input().rstrip()

is_bomb = True

while is_bomb:
    is_bomb = False
    stack = []
    
    for i in range(len(s_arr)):
        if s_arr[i] == bomb_str[len(stack)]:
            if len(stack) != 0 and s_arr[i - 1] == bomb_str[len(stack) - 1]:
                stack.append(s_arr[i])
            elif len(stack) == 0:
                stack.append(s_arr[i])

        if ''.join(stack) == bomb_str:
            is_bomb = True
            
            new_str = s_arr[:i - (len(stack) - 1)] + s_arr[i + 1:]
            s_arr = new_str
            break

if len(s_arr) == 0:
    print("FRULA")
else:
    print(s_arr)