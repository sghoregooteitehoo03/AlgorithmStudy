n = int(input())
traveler = list(map(int, input().split()))
result = 0
i = 0
traveler.sort(reverse=True)

while i < n:
    cost = traveler[i]
    rangeVal = (i + cost)

    if(rangeVal) <= n:
        group = traveler[i:rangeVal]

        if len(group) == cost:
            result += 1
            i = (rangeVal - 1)
    
    i += 1

print(result)