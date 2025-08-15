import itertools

l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
condition = ['a', 'e', 'i', 'o', 'u']

for x in itertools.combinations(arr, l):
    count1 = 0
    count2 = 0
    for password in list(x):
        if password in condition:
            count1 += 1
        else:
            count2 += 1
            
    if count1 >= 1 and count2 >= 2:
        print(''.join(list(x)))