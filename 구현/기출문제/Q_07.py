# https://www.acmicpc.net/problem/18406
n = input()
half = len(n) // 2

first = list(map(int, n[:half]))
second = list(map(int, n[half:]))

if sum(first) == sum(second):
    print("LUCKY")
else:
    print("READY")

# str = input()
# half = len(str) // 2

# part1 = str[:half]
# part2 = str[half:]
# part1_sum = 0
# part2_sum = 0

# for i in range(half):
#     n1 = int(part1[i])
#     n2 = int(part2[i])
#     part1_sum += n1
#     part2_sum += n2

# if part1_sum == part2_sum:
#     print("LUCKY")
# else:
#     print("READY")