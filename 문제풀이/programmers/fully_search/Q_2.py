# 문제의 개수만큼 각 수포자의 배열도 늘림

def solution(answers):
    answer = []
    person_1 = [1, 2, 3, 4, 5] * (len(answers) + 1)
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) + 1)
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) + 1)

    person1_count = 0
    person2_count = 0
    person3_count = 0
    
    for i in range(len(answers)):
        number = answers[i]

        if person_1[i] == number:
            person1_count += 1

        if person_2[i] == number:
            person2_count += 1

        if person_3[i] == number:
            person3_count += 1

    max_value = max(person1_count, person2_count, person3_count)
    
    if person1_count == max_value:
        answer.append(1)
    
    if person2_count == max_value:
        answer.append(2)

    if person3_count == max_value:
        answer.append(3)

    return answer


solution([1, 2, 3, 4, 5])
solution([1, 2, 3, 4, 5, 3, 2, 1, 3, 4, 5, 5, 3, 2, 1, 2, 3, 4])