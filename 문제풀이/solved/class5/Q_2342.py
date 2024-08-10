import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr.pop(-1)

if len(arr) == 0:
    print(0)
elif len(arr) < 2:
    print(2)
else:
    dp = [[] for _ in range(len(arr))]
    history = [[-1] * 5 for _ in range(5)]

    dp[0].append((arr[0], 0, 2))
    history[arr[0]][0] = 0

    for i in range(1, len(arr)):
        for previous_value in dp[i - 1]:
            dest = arr[i]
            x, y, count = previous_value

            if history[x][y] != i and history[y][x] != i:
                if x == dest or y == dest:
                    history[x][y] = i
                    dp[i].append((x, y, count + 1))
                else:
                    x_count = 0
                    y_count = 0

                    if abs(x - dest) == 2:
                        x_count = count + 4
                    else:
                        x_count = count + 3

                    if y == 0:
                        y_count = count + 2
                    else:
                        if abs(y - dest) == 2:
                            y_count = count + 4
                        else:
                            y_count = count + 3

                    history[dest][y] = i
                    history[x][dest] = i

                    dp[i].append((dest, y, x_count))
                    dp[i].append((x, dest, y_count))
    print(min(dp[-1], key= lambda x: x[2])[2])

# 2 1 3 2 3 0
