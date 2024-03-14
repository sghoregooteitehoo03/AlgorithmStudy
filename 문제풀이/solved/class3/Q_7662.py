import heapq

t = int(input())
for i in range(t):
    max_q = []
    min_q = []

    k = int(input())
    first = True
    for j in range(k):
        case, n = input().split()
        number_n = int(n)

        if case == 'D':    
            if number_n < 0:
                if len(min_q) != 0:
                    heapq.heappop(min_q)
            else:
                if len(max_q) != 0:
                    heapq.heappop(max_q)
        
        elif case == 'I':
            if number_n < 0:
                heapq.heappush(min_q, number_n)
            else:
                heapq.heappush(max_q, -number_n)

    max_value = -1
    min_value = -1

    if len(max_q) >= 2 and len(min_q) == 0:
        max_value = (heapq.heappop(max_q)) * -1
        min_value = max(max_q) * -1
    elif len(max_q) == 0 and len(min_q) >= 2:
        max_value = max(min_q)
        min_value = (heapq.heappop(min_q))
    elif len(max_q) > 0 and len(min_q) > 0:
        max_value = (heapq.heappop(max_q)) * -1
        min_value = (heapq.heappop(min_q))

    if max_value != -1 and min_value != -1:
        print(max_value, min_value)
    else:
        print("EMPTY")