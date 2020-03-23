N = int(input())
G = [list(map(int, input().split())) for i in range(N)]

ans = float('inf')

dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]


def f(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // N
        y = flower % N
        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            return float('inf')
        for w in range(5):
            flow.append((x + dx[w], y + dy[w]))
            ret += G[x + dx[w]][y + dy[w]]

    if len(set(flow)) != 15:
        return float('inf')
    return ret


for i in range(N * N):
    for j in range(i + 1, N * N):
        for k in range(j + 1, N * N):
            ans = min(ans, f([i, j, k]))

print(ans)