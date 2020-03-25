from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Q = [list(map(int, input().split())) for _ in range(K)]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]  # 남 서 북 동

ans = 1000000


def value(arr):
    return min([sum(i) for i in arr])


def convert(arr, qry):
    (r, c, s) = qry
    r, c = r - 1, c - 1
    new_arr = deepcopy(arr)
    for i in range(1, s + 1):
        rr, cc = r - i, c + i
        for w in range(4):
            for d in range(i * 2):
                rrr, ccc = rr + dx[w], cc + dy[w]
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return new_arr


def dfs(arr, qry):
    global ans
    if sum(qry) == K:
        ans = min(ans, value(arr))
        return
    for i in range(K):
        if qry[i]:
            continue
        new_arr = convert(arr, Q[i])
        qry[i] = 1
        dfs(new_arr, qry)
        qry[i] = 0


dfs(A, [0 for i in range(K)])
print(ans)
