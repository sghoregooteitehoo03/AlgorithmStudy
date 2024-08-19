def solution(nums):
    n = len(nums) // 2
    pokemon = set(nums)

    if len(pokemon) < n:
        return len(pokemon)
    else:
        return n

arr1 = [3, 1, 2, 3]
arr2 = [3, 3, 3, 2, 2, 4]
arr3 = [3, 3, 3, 2, 2, 2]

print(solution(arr1))
print(solution(arr2))
print(solution(arr3))