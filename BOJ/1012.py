from collections import deque


def bfs(start_node, N, M):
    need_visit = deque([start_node])
    visited = deque()

    while need_visit:
        node = need_visit.popleft()
        if node not in visited and array[node[0]][node[1]] is True:
            visited.append(node)
            for a, b in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                array[node[0]][node[1]] = None
                if 0 <= node[0] + a < N and 0 <= node[1] + b < M:
                    need_visit.append([node[0] + a, node[1] + b])

    return visited


test_case = int(input())
for _ in range(test_case):
    M, N, K = list(map(int, input().split()))
    array = [[None] * M for _ in range(N)]

    for _ in range(K):
        row_num, col_num = list(map(int, input().split()))
        array[col_num][row_num] = True

    count = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if bfs([i - 1, j - 1], N, M):
                count += 1
    print(count)
