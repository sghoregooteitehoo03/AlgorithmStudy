import copy

def possible_pillar(arr, i, j):
    is_possible = False
    
    if i == 0:
        is_possible = True
    else:
        if arr[i - 1][j] == '|':
            is_possible = True
        else:
            if j + 1 < len(arr):
                if arr[i][j + 1] == '-':
                    is_possible = True
                else:
                    is_possible = False
            
            if not is_possible and j - 1 >= 0:
                if arr[i][j - 1] == '-':
                    is_possible = True
                else:
                    is_possible = False

    return is_possible

def possible_line(arr, i, j):
    is_possible = False

    if arr[i - 1][j] == '|':
        is_possible = True
    else:
        if j + 1 < len(arr) and arr[i-1][j + 1]:
            is_possible = True
        else:
            if j + 1 < len(arr) and j - 1 >= 0:
                if(arr[i][j + 1] == '-' and arr[i][j - 1] == '-'):
                    is_possible = True
                    
                else:
                    is_possible = False
            else:
                is_possible = False

    return is_possible

def is_possible_remove(arr, answer_arr, i, j):
    is_possible = False
    reanswer = []

    for answer in answer_arr:
        if answer[1] != i or answer[0] != j:
            if answer[2] == 0:
                is_possible = possible_pillar(arr, answer[1], answer[0])
                reanswer.append(answer)
                if is_possible == False:
                    break
            else:
                is_possible = possible_line(arr, answer[1], answer[0])
                reanswer.append(answer)
                if is_possible == False:
                    break
    
    if is_possible: 
        return [is_possible, reanswer]
    else:
        return [is_possible, answer_arr]


def solution(n, build_frame):
    struc_arr = [[''] * (n + 1) for _ in range(n + 1)]
    answer = []

    for build in build_frame:
        if build[3] == 1: # 설치
            if build[2] == 0:  # 기둥일 경우 |
                if possible_pillar(struc_arr, build[1], build[0]):
                    struc_arr[build[1]][build[0]] = '|'
                    answer.append([build[0], build[1], build[2]])

            else:  # 보 일 경우 -
                if possible_line(struc_arr, build[1], build[0]):
                    struc_arr[build[1]][build[0]] = '-'
                    answer.append([build[0], build[1], build[2]])

        else: # 지우기
            copy_struc = copy.deepcopy(struc_arr)

            if build[2] == 0 and struc_arr[build[1]][build[0]] == '|':
                copy_struc[build[1]][build[0]] = ''
                result = is_possible_remove(copy_struc, answer, build[1], build[0])
                if result[0]:
                    struc_arr = copy_struc
                    answer = result[1]
            elif build[2] == 1 and struc_arr[build[1]][build[0]] == '-':
                copy_struc[build[1]][build[0]] = ''

                result = is_possible_remove(copy_struc, answer, build[1], build[0])
                if result[0]:
                    struc_arr = copy_struc
                    answer = result[1]

    sorted_data = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return sorted_data

solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
# solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
