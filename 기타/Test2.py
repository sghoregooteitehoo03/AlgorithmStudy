from itertools import combinations

l, c = map(int, input().split())
ap_list = list(input().split())
ap_list.sort()

combine = combinations(ap_list, l)
result = 0
for data in combine:
    consonants = 0 # 자음
    vowels = 0 # 모음
    
    for C in data:
        if C == 'a' or C == 'e' or C == 'i' or C == 'o' or C == 'u':
            vowels += 1
        else:
            consonants += 1
    
    if vowels >= 1 and consonants >= 2:
        print(''.join(map(str, data)))