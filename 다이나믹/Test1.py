# from collections import deque

# n = int(input())
# queue = deque([n])
# result = 0
# isBreak = False

# while not isBreak:    
#     for i in range(len(queue)):
#         data = queue.popleft()

#         if data == 1:
#             result -= 1
#             isBreak = True

#             break

#         queue.append(data - 1)

#         if data % 5 == 0:
#             queue.append((data // 5))
    
#         if data % 3 == 0:
#             queue.append(data // 3)

#         if data % 2 == 0:
#             queue.append(data // 2)
    
#     result += 1

# print(result)


# 답지
# x = int(input())
# d = [0] * 30001

# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)
#     print(i, d[i])

# print(d[x])