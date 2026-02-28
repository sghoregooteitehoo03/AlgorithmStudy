# 문자열을 가지고 만들 수 있는 모든 조합을 만듬
# int로 변환시켜 소수인지를 판별해 카운트

from itertools import permutations
import math

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    unique_numbers = set()

    for i in range(1, len(numbers) + 1):
        for data in permutations(numbers, i):
            number = int("".join(data))
            unique_numbers.add(number)

    for number in unique_numbers:
        if is_prime(number):
            answer += 1

    return answer