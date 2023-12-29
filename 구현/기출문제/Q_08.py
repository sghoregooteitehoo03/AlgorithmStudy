str = input()
sum = 0
index = -1
sortedArray = sorted(str)

for i in range(len(sortedArray)):
    s = sortedArray[i]
    if s.isdigit():
        sum += int(s)
    else:
        index = i
        break

print("".join(sortedArray[i:len(sortedArray)]) + sum.__str__())