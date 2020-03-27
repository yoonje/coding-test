import copy

N, A = int(input()), list(map(int, input().split()))
# dp[i]는 i까지 왔을 때 합의 최대
dp = copy.deepcopy(A)

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(A[i] + dp[j], dp[i])

print(max(dp))
