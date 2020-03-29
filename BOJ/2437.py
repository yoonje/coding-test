N, A = int(input()), sorted(list(map(int, input().split())))

# 만들 수 있는 최저
ans = 0

for i in A:
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans + 1)
