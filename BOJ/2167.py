N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for i in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + A[i - 1][j - 1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1])
