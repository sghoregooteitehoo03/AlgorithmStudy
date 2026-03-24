N, B = map(int, input().split())
arr = []

while N > 0:
    arr.append(N % B)
    N //= B

arr.reverse()
for n in arr:
    if 10 <= n:
        print(chr(n + 55), end="")
    else:
        print(n, end="")
print()