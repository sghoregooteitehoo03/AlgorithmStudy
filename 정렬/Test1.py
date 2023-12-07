n = int(input())
array = []

for i in range(n):
    input_data = int(input())
    array.append(input_data)

array.sort(reverse=True)
for i in array:
    print(i, end=' ')
