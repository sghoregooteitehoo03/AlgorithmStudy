# https://www.youtube.com/watch?v=E6W0ySoRygQ&ab_channel=%EC%9D%80%EC%84%9C%ED%8C%8C%EC%9D%98%EB%8C%80%EC%B6%A9APS
import heapq
import sys
input = sys.stdin.readline

n = int(input())
left = []
right = []
result = []

for i in range(n):
    i_data = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -i_data)
    else:
        heapq.heappush(right, i_data)

    if len(right) != 0 and -left[0] > right[0]:
        heapq.heappush(left, -heapq.heappop(right))
        heapq.heappush(right, -heapq.heappop(left))
    
    result.append(-left[0])

for r in result:
    print(r)