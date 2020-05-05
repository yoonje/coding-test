import re
from itertools import permutations


def solution(user_id, banned_id):
    banned_id = [item.replace("*", ".") for item in banned_id]
    answer = []
    banned_len = len(banned_id)
    permuted = permutations(user_id, banned_len)
    for user_arr in permuted:
        cnt = 0
        for i in range(banned_len):
            if re.search("^" + banned_id[i] + "$", user_arr[i]):
                cnt += 1
        sorted_user = sorted(user_arr)
        if cnt == banned_len and sorted_user not in answer:
            answer.append(sorted_user)
    return len(answer)
