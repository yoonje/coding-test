def solution(sticker):
    len_sticker = len(sticker)
    if len(sticker) == 1:
        return sticker[0]

    dp = [0 for _ in range(len_sticker)]
    dp2 = [0 for _ in range(len_sticker)]

    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, len_sticker - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])

    dp2[1] = sticker[1]
    for i in range(2, len_sticker):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    max1 = max(dp)
    max2 = max(dp2)
    return max(max1, max2)


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))  # 36
print(solution([1, 3, 2, 5, 4]))  # 8
