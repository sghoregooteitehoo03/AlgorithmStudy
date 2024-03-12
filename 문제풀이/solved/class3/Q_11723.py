import sys
input = sys.stdin.readline

arr = {}
def add(x):
    arr[x] = 1

def remove(x):
    if arr.get(x) != None:
        del arr[x]

def check(x):
    if arr.get(x) != None:
        print(1)
    else:
        print(0)

def toggle(x):
    if arr.get(x) != None:
        remove(x)
    else:
        add(x)

def all():
    for i in range(1, 21):
        add(i)

def empty():
    arr.clear()

m = int(input())
for i in range(m):
    s = input().replace('\n', '')
    s = s.split(' ')
    command = s[0]
    
    if len(s) == 1:
        if command == 'all':
            all()
        elif command == 'empty':
            empty()
    else:
        x = int(s[1])

        if command == 'add':
            add(x)
        elif command == 'remove':
            remove(x)
        elif command == 'check':
            check(x)
        elif command == 'toggle':
            toggle(x)