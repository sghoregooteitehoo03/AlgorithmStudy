# https://www.acmicpc.net/problem/1715
import heapq

n = int(input())
queue = []

for i in range(n):
    heapq.heappush(queue, int(input()))

result = 0
while queue:
    q1 = heapq.heappop(queue)

    if len(queue) >= 1:
        q2 = heapq.heappop(queue)
        result += q1 + q2

        heapq.heappush(queue, q1 + q2)

print(result)

# import heapq

# n = int(input())
# array = []
# result = 0

# for i in range(n):
#     array.append(int(input()))

# if n == 1:
#     print(0)
# else:
#     q = []
#     for a in array:
#         heapq.heappush(q, a)

#     while(q):
#         val1 = heapq.heappop(q)

#         if len(q) != 0:
#             val2 = heapq.heappop(q)

#             result += (val1 + val2)
#             heapq.heappush(q, val1 + val2)

#     print(result)
