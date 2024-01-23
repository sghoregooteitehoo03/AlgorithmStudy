# https://www.acmicpc.net/problem/1715
import heapq

n = int(input())
array = []
result = 0

for i in range(n):
    array.append(int(input()))

if n == 1:
    print(0)
else:
    q = []
    for a in array:
        heapq.heappush(q, a)

    while(q):
        val1 = heapq.heappop(q)
        
        if len(q) != 0:
            val2 = heapq.heappop(q)
            
            result += (val1 + val2)
            heapq.heappush(q, val1 + val2)

    print(result)