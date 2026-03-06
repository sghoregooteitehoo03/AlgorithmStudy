# target이 words에 있는지 여부먼저 확인 없으면 로직 수행
# begin을 words에 있는 문자들과 한 글자씩 판별해 바꿀 수 있는 걸 큐에 담으면서 카운팅
# 반복해서 target이 되는걸 찾고 카운트 반환
from collections import deque
INF = 1e9

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    history = {}
    
    answer = INF
    while queue:
        begin_word, count = deque.popleft(queue)

        if begin_word == target:
            answer = min(answer, count)

        if history.get(begin_word) != None:
            continue

        history[begin_word] = True

        count_dict = {}
        for i in range(len(begin_word)):
            for word in words:
                if begin_word[i] != word[i]:
                    if count_dict.get(word) == None:
                        count_dict[word] = 1
                    else:
                        count_dict[word] = count_dict[word] + 1

        for key, values in count_dict.items():
            if values == 1:
                queue.append((key, count + 1))
    
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))