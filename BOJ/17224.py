N, L, K = map(int, input().split())

easy_count, hard_count = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard_count += 1
    elif sub1 <= L < sub2:
        easy_count += 1

score = min(hard_count, K) * 140
score += min(easy_count, K - hard_count) * 100

print(score)
