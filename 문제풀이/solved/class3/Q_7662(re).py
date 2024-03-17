import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    max_q = []
    min_q = []
    k = int(input())
    check = [1] * k

    for i in range(k):
        case, n = input().split()
        number_n = int(n)

        if case == 'I':
            heapq.heappush(min_q, (number_n, i))
            heapq.heappush(max_q, (-number_n, i))
        else:
            if number_n == -1:
                if min_q:
                    check[heapq.heappop(min_q)[1]] = 0
            elif number_n == 1:
                if max_q:
                    check[heapq.heappop(max_q)[1]] = 0
    
        while min_q and check[min_q[0][1]] == 0:
            heapq.heappop(min_q)
        while max_q and check[max_q[0][1]] == 0:
            heapq.heappop(max_q)
    
    if min_q == []:
        print("EMPTY")
    else:
        print(-max_q[0][0], min_q[0][0])