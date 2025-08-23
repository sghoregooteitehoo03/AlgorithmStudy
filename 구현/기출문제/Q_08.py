s = input()
arr = list(map(str, s))
arr.sort()

total = 0
for i in range(len(arr)):
    if arr[i].isdigit():
        total += int(arr[i])
    else:
        break
    
print("".join(arr[i:]) + str(total))

# str = input()
# sum = 0
# index = -1
# sortedArray = sorted(str)

# for i in range(len(sortedArray)):
#     s = sortedArray[i]
#     if s.isdigit():
#         sum += int(s)
#     else:
#         index = i
#         break

# print("".join(sortedArray[i:len(sortedArray)]) + sum.__str__())