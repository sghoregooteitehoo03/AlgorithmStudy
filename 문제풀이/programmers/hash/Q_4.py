def solution(clothes):
    answer = 0
    sorted_cloth = {}

    for i in range(len(clothes)):
        cloth, type = clothes[i]
        if sorted_cloth.get(type) == None:
            sorted_cloth[type] = [cloth]
        else:
            sorted_cloth[type].append(cloth)

    for key in sorted_cloth.keys():
        cloth_count = len(sorted_cloth[key])
        answer = answer + (answer * cloth_count) + cloth_count
    
    return answer


clothes1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes1))
print(solution(clothes2))