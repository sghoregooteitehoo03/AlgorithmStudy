# 그리디 문제
# 손에 일단 집어넣고 조건들을 비교
# 손에 있는걸로 조합이 되는지, 손에있는것과 카드 하나로 조합이 되는지, 가져온 카드들로 조합이 되는지
# 그게 다 안되면 끝

def solution(coin, cards):
    n = len(cards)
    target = n + 1

    hand = set(cards[:n // 3])
    deck = cards[n // 3:]
    keep = set()

    def find_and_remove(set1, set2):
        for card in list(set1):
            matching_card = target - card

            if matching_card in set2:
                set1.remove(card)
                set2.remove(matching_card)
                return True
        return False

    idx = 0
    round = 1

    while idx < len(deck):
        keep.add(deck[idx])
        keep.add(deck[idx + 1])
        idx += 2

        if find_and_remove(hand, hand):
            pass
        elif coin >= 1 and find_and_remove(hand, keep):
            coin -= 1
        elif coin >= 2 and find_and_remove(keep, keep):
            coin -= 2
        else:
            break

        round += 1

    return round


print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
