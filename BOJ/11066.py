def process():
    N, A = int(input()), [0] + list(map(int, input().split()))
    # S[i]는 1번부터 i번까지의 누적합
    S = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        S[i] = S[i - 1] + A[i]

    # dp[i][j]는 i에서 j까지 합하는데 필요한 최소 비용
    # dp[i][k] + dp[k+1][j] + sum(A[i]~A[j])
    dp = [[0 for i in range(N + 1)] for _ in range(N + 1)]
    for i in range(2, N + 1):  # 부분 배열 길이
        for j in range(1, N + 2 - i):  # 시작점
            dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + S[j + i - 1] - S[
                j - 1]

    print(dp[1][N])


for _ in range(int(input())):
    process()
