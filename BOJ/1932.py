N = int(input())
A = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# dp[i][j]는 i,j를 도착했을 때 최대값
# dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + A[i][j]
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    for j in range(1, i + 1):
        A[i][j] = tmp[j - 1]

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + A[i][j]

print(max(dp[-1]))
