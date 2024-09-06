import heapq

def solution(jobs):
    answer = 0
    time_table = {}

    for timing, end_time in jobs:
        if time_table.get(timing) != None:
            time_table[timing].append((end_time, timing))
        else:
            time_table[timing] = [(end_time, timing)]

    q = []
    start_time = -1
    end_time = -1
    time = 0 

    while time < 500001:
        if time_table.get(time) != None:
            for e_t, s_t in time_table[time]:
                heapq.heappush(q, (e_t, s_t))

            if start_time == -1 and end_time == -1:
                end_time, start_time = heapq.heappop(q)
                end_time += time

        if end_time == time:
            answer += (time - start_time)
            
            if len(q) != 0:
                end_time, start_time = heapq.heappop(q)
                end_time += time
            else:
                start_time = -1
                end_time = -1

        time += 1

    answer //= len(jobs)
    return answer


# solution([[0, 3], [1, 9], [2, 6]])
# solution([[0, 1], [0, 2], [1, 6]])
solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])
# solution([[1,4],[7,9],[1000,3]])