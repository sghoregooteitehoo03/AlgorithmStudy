def solution(word):
    count = 0
    step = ["A", "E", "I", "O", "U"]
    word_1 = ""
    word_2 = ""
    word_3 = ""
    word_4 = ""
    word_5 = ""

    for a in range(5):
        word_1 = step[a]
        count += 1

        if word_1 == word:
            return count

        for e in range(5):
            word_2 = step[e]
            count += 1

            total_word = word_1 + word_2
            if total_word == word:
                return count

            for i in range(5):
                word_3 = step[i]
                count += 1

                total_word = word_1 + word_2 + word_3
                if total_word == word:
                    return count

                for o in range(5):
                    word_4 = step[o]
                    count += 1

                    total_word = word_1 + word_2 + word_3 + word_4
                    if total_word == word:
                        return count

                    for u in range(5):
                        word_5 = step[u]
                        count += 1

                        total_word = word_1 + word_2 + word_3 + word_4 + word_5
                        if total_word == word:
                            return count

print(solution("AAAAE"))
print(solution("AAAE"))  # 10
print(solution("AAAI"))  # 16
print(solution("I"))
print(solution("EIO"))
