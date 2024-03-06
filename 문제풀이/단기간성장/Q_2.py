import heapq
import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    i_data = int(input())
    heapq.heappush(data, i_data)
    heapq.heapify(data)
    
    print(data)
    # if (i + 1) % 2 == 0:
    #     print(data[((i + 1) // 2) - 1])
    # else:
    #     print(data[((i + 1) // 2)])