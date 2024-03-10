# https://www.acmicpc.net/problem/7568
n = int(input())
data = []
result = []

for i in range(n):
    weight, height = map(int, input().split())
    data.append((weight, height))

for i in range(n):
    rank = 1

    for j in range(n):
        if i == j:
            continue
        
        if(data[i][0] > data[j][0] and data[i][1] > data[j][1]):
            continue
        elif (data[i][0] < data[j][0] and data[i][1] < data[j][1]):
            rank += 1
        
    result.append(rank)

for r in result:
    print(r, end=' ')