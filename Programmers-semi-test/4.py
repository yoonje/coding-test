def solution(board):
    ans = 0
    dp = [[0] * 1001 for _ in range(1001)]
    for row in range(1, len(board) + 1):
        for col in range(1, len(board[0]) + 1):
            if board[row - 1][col - 1] != 0:
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
                ans = max(ans, dp[row][col])
    return ans * ans
