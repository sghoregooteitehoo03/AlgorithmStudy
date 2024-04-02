import sys
input = sys.stdin.readline

n, m = map(int, input().split())
peoples = [False] * (n + 1)
party_arr = []
result = 0

truth = list(map(int, input().split()))
for i in range(len(truth)):
    if i == 0:
        continue

    peoples[truth[i]] = True

for i in range(m):
    arr = list(map(int, input().split()))
    arr.pop(0)

    party_arr.append(arr)

for party in party_arr:
    is_fine = True
    
    for people in party:
        if peoples[people]:
            is_fine = False
            break

    if is_fine:
        result += 1

print(result)