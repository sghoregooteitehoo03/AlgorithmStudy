import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    x = int(input())
    
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if len(arr) != 0:
            print(heapq.heappop(arr)[1])
        else:
            print(0)