def solution(land):
    row = len(land[0])
    dp = [[0] * 4] * 100000
    dp[0] = land[0][:]
    for i in range(len(land) - 1):
        for j in range(row):
            dp[i + 1][j] = int(max(dp[i][(j + 1) % 4], dp[i][(j + 2) % 4], dp[i][(j + 3) % 4]) + land[i + 1][j])
    return max(dp[i + 1])
