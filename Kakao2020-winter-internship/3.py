import re
from itertools import permutations


def solution(user_id, banned_id):
    banned_id = [item.replace("*", ".") for item in banned_id]
    answer = []
    user_len, banned_len = len(user_id), len(banned_id)
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


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))  # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))  # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))  # 3
