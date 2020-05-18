from collections import defaultdict


def solution(clothes):
    cloth_dict = defaultdict(int)
    for item in clothes:
        cloth_dict[item[1]] += 1
    answer = 1
    for i in cloth_dict.values():
        answer *= i + 1
    return answer - 1
