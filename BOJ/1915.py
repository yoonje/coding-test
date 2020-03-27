N, M = map(int, input().split())
array = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
# dp[i][j]는 i,j까지 왔을 때, 가장 큰 정사각형의 한 변의 길이
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] dp[i][j-1]) + 1
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N):
    for idx, j in enumerate(list(map(int, list(input())))):
        array[i + 1][idx + 1] = j

mx = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if array[i][j]:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
            mx = max(dp[i][j], mx)

print(mx ** 2)
