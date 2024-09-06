import heapq

def solution(operations):
    answer = []
    q_max = []
    q_min = []

    for operation in operations:
        type, number = operation.split(" ")
        number = int(number)
        
        if type == "I":
            if number < 0:
                heapq.heappush(q_min, number)
                heapq.heappush(q_max, number)
            else:
                heapq.heappush(q_max, -number)
                heapq.heappush(q_min, number)

        elif type == "D":
            if number < 0:
                if len(q_min) != 0:
                    heapq.heappop(q_min)
                else:
                    heapq.heappop(q_max)

            else:
                if len(q_max) != 0:
                    heapq.heappop(q_max)
                else:
                    heapq.heappop(q_min)
    
    print(q_max)
    print(q_min)
    return answer

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])