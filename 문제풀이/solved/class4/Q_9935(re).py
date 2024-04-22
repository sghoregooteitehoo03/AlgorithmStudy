import sys
input = sys.stdin.readline

s_arr = input().strip()
bomb_str = input().strip()

bomb_str_len = len(bomb_str)
stack = []
    
for i in range(len(s_arr)):
    stack.append(s_arr[i])
    
    if ''.join(stack[-bomb_str_len:]) == bomb_str:
        for j in range(bomb_str_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")