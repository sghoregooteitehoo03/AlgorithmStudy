def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    
    history = { phone_book[0] : True }
    len_history = [len(phone_book[0])]

    for i in range(1, len(phone_book)):
        phone_num = phone_book[i]

        for num_len in len_history:
            if history.get(phone_num[:num_len]) != None:
                answer = False
                break

        if not answer:
            break

        previous_len = len_history[-1]
        current_len = len(phone_num)
        history[phone_num] = True

        if previous_len < current_len:
            len_history.append(len(phone_num))
    return answer

test1 = ["119", "97674223", "1195524421"]	
test2 = ["123","456","789"]	
test3 = ["12","123","1235","567","88"]	
print(solution(test1))
print(solution(test2))
print(solution(test3))