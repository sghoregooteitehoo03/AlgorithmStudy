# https://www.acmicpc.net/contest/problem/1244/1

t = int(input())
data = []

for i in range(t):
    data.append(input())

for str in data:
    n = False
    a = str.split('0')
    if len(a) == 1:
        n = True
        a = str.split('1')
    
    if a[0] != '':
        if len(a[0]) % 2 == 0:
            if a[1] != '':
                print(1)
            else:
                print(int(n))
        else:
            if a[1] != '':
                n = True

            n = not n
            print(int(n))
    elif a[1] != '':
        print(1)
    else:
        print(int(n))