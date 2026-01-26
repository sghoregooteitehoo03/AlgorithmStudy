def solution(food_times, k):
    values = []
    n = len(food_times)

    for i in range(n):
        values.append((food_times[i], i + 1))

    values.sort()
    pretime = 0
    for i in range(len(values)):
        food = values[i]
        diff = food[0] - pretime

        if diff != 0:
            spend = diff * n

            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(values[i:], key=lambda x: x[1])
                return sublist[k][1]

        n -= 1

    return -1


# def solution(food_times, k):
#     values = []
#     n = len(food_times)

#     for i in range(len(food_times)):
#         values.append((food_times[i], i + 1))

#     values.sort()
#     pretime = 0
#     for i in range(len(food_times)):
#         food = values[i]
#         diff = food[0] - pretime

#         if diff != 0:
#             spend = diff * n

#             if spend <= k:
#                 k -= spend
#                 pretime = food[0]
#             else:
#                 k %= n
#                 sublist = sorted(values[i:], key= lambda x: x[1])
#                 return sublist[k][1]

#         n -= 1

#     return -1

# def solution(food_times, k):
#     foods = []
#     n = len(food_times)

#     for i in range(n):
#         foods.append((food_times[i], i+1))

#     foods.sort()
#     previous_t = 0

#     for i, food in enumerate(foods):
#         diff = food[0] - previous_t
#         if diff != 0:
#             spend = diff * n
#             if spend <= k:
#                 k -= spend
#                 previous_t = food[0]
#             else:
#                 k %= n
#                 sublist = sorted(foods[i:], key=lambda x: x[1])
#                 return sublist[k][1]
#         n -= 1

#     return -1


# import heapq

# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1

#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i + 1))

#     sum_value = 0
#     previous = 0

#     length = len(food_times)
#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now

#     result = sorted(q, key =lambda x: x[1])
#     return result[(k - sum_value) % length][1]
