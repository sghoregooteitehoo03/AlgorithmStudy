n, k = map(int, input().split())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

sorted_A = sorted(array_A)
sorted_B = sorted(array_B, reverse=True)

for i in range(k):
    sorted_A[i], sorted_B[i] = sorted_B[i], sorted_A[i]

print(sum(sorted_A))