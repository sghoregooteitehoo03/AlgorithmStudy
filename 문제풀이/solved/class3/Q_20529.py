from itertools import combinations
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    persons = list(input().split())
    result = 1e9
    history = {}
    
    persons.sort()
    print(persons)
    
    for combination in list(combinations(persons, 3)):
        cal = 0
        
        if history.get(combination) != None:
            continue
        else:
            history[combination] = True

        for diff in list(combinations(combination, 2)):
            if history.get(diff) != None:
                cal1 = history[diff]
                cal += cal1
            else:
                cal2 = 0
                for i in range(4):
                    if diff[0][i] != diff[1][i]:
                        cal2 += 1
                
                history[diff] = cal2
                cal += cal2
        
        if result > cal:
            result = cal

    print(result)