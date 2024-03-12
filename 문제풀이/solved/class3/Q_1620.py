data = {}
n, m = map(int, input().split())

for i in range(1, n + 1):
    name = input()
    
    data[i.__str__()] = name
    data[name] = i

for i in range(m):
    q = input()
    print(data[q])