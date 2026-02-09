# https://www.acmicpc.net/problem/18310
n = int(input())
house = list(map(int, input().split()))
house.sort()

if len(house) % 2 == 0:
    print(house[(len(house) // 2) - 1])
else:
    print(house[(len(house) // 2)])