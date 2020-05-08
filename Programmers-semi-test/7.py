def solution(strs, t):
    max_word_len = max([len(x) for x in strs])
    dp = [10000000000] * len(t)
    dp = dp + [0] * max_word_len
    for index in range(len(t) - 1, -1, -1):
        for m in range(max_word_len):
            tmp_index = m + index
            if t[index:tmp_index + 1] in strs:
                dp[index] = min(dp[index], dp[tmp_index + 1] + 1)
    if dp[0] == 10000000000:
        return -1
    return dp[0]

