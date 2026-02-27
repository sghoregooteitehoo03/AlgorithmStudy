# 배열 슬라이싱
# 정렬
# 해당 인덱스 값 출력


def solution(array, commands):
    answer = []

    for t in commands:
        slicing_i, slicing_j, index = t
        sliced_arr = array[slicing_i - 1 : slicing_j]
        sliced_arr.sort()

        answer.append(sliced_arr[index - 1])

    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
