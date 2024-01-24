# https://www.acmicpc.net/problem/2110
import copy
def set_access_point(arr, result, start, end, C):
    if start > end:
        return None

    global point
    
    mid_index = (start + end) // 2
    
    if C % 2 == 0 and (mid_index + 1) % 2 == 0:
        result.append(arr[mid_index])
    elif C % 2 != 0 and (mid_index + 1) % 2 != 0:
        result.append(arr[mid_index])




N, C = map(int, input().split())
point = 0
home_pos = []
result = []

for i in range(N):
    home_pos.append(int(input()))

home_pos.sort()
home_sub_pos = copy.deepcopy(home_pos)
for i in range(C):
    mid = len(home_sub_pos) // 2
    
    result.append(home_pos[mid])
    slice_len1 = len(home_sub_pos[0:mid])
    slice_len2 = len(home_sub_pos[mid:len(home_sub_pos)])

    if slice_len1 > slice_len2:

    elif slice_len2 > slice_len1:
    eles:

# 1 2 4 8 9
# 1 2 4 8