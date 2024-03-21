from itertools import product
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
broken_buttons = []

if m != 0:
    broken_buttons = list(map(int, input().split()))

for broken_button in broken_buttons:
    buttons.remove(broken_button)

combine = list(product(buttons, repeat=1))
combine += list(product(buttons, repeat=2))
combine += list(product(buttons, repeat=3))
combine += list(product(buttons, repeat=4))
combine += list(product(buttons, repeat=5))
combine += list(product(buttons, repeat=6))

min_number = 100
max_number = 100
result = 1e9
for data in combine:
    number = int(''.join(map(str, data)))
    
    if number > n:
        max_number = number
        break
    else:
        min_number = number

if n - min_number >= 0 and result > len(str(min_number)) + (n - min_number):
    result = len(str(min_number)) + (n - min_number)
if max_number - n >= 0 and result > len(str(max_number)) + (max_number - n):
    result = len(str(max_number)) + (max_number - n)
if n - 100 >= 0 and result > n - 100:
    result = n - 100
if 100 - n >= 0 and result > 100 - n:
    result = 100 - n

print(result)