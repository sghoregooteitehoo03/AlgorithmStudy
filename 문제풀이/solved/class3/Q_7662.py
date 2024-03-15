import heapq

t = int(input())
for i in range(t):
    max_q = []
    heapq.heapify(max_q)
    min_q = []
    heapq.heapify(min_q)

    k = int(input())
    for j in range(k):
        case, n = input().split()
        number_n = int(n)

        if case == 'D':    
            if number_n < 0:
                if len(min_q) > 0:
                    heapq.heappop(min_q)
                elif len(max_q) > 0:
                    max_q = [-x for x in max_q]
                    heapq.heapify(max_q)
                    heapq.heappop(max_q)

                    if len(max_q) > 0:
                        max_q = [-x for x in max_q]
                        heapq.heapify(max_q)
            else:
                if len(max_q) > 0:
                    heapq.heappop(max_q)
                elif len(min_q) > 0:
                    min_q = [-x for x in min_q]
                    heapq.heapify(min_q)
                    heapq.heappop(min_q)

                    if len(min_q) > 0:
                        min_q = [-x for x in min_q]
                        heapq.heapify(min_q)
        
        elif case == 'I':
            if number_n < 0:
                heapq.heappush(min_q, number_n)
            else:
                heapq.heappush(max_q, -number_n)

    max_value = None
    min_value = None

    if len(max_q) > 0 and len(min_q) == 0:
        max_value = -(heapq.heappop(max_q))

        if len(max_q) != 0:
            max_q = [-x for x in max_q]
            heapq.heapify(max_q)

            min_value = heapq.heappop(max_q)
        else:
            min_value = max_value
    elif len(max_q) == 0 and len(min_q) > 0:
        min_value = heapq.heappop(min_q)
        
        if len(min_value) != 0:
            min_q = [-x for x in min_q]
            heapq.heapify(min_q)

            max_value = heapq.heappop(min_q)
        else:
            max_value = min_value
            
    elif len(max_q) > 0 and len(min_q) > 0:
        max_value = -(heapq.heappop(max_q))
        min_value = heapq.heappop(min_q)

    if max_value != None and min_value != None:
        print(max_value, min_value)
    else:
        print("EMPTY")
        