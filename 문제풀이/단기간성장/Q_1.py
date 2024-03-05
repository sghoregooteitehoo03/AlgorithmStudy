from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for i in range(n):
    w, v = map(int, input().split())
    
    arr.append((w, v))

arr.sort()
max_value = 0

for i in range(1, n + 1):
    combine = combinations(arr, i)
    dict = {}
    
    for c in combine:
        weight = 0
        cal_value = 0

        if dict.get(c) != None:
            break
        else:
            dict[c] = 1

        for j in range(len(c)):
            weight += c[j][0]
            cal_value += c[j][1]
        
        if weight <= k:
            if max_value < cal_value:
                max_value = cal_value
        else:
            break

print(max_value)