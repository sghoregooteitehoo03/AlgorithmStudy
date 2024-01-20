n = int(input())
home = list(map(int, input().split()))

home.sort()

if len(home) % 2 == 0:
    print(home[(len(home) // 2) - 1])
else:
    print(home[len(home) // 2])