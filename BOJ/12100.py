from copy import deepcopy


def rotate90(board, N):
    new_board = deepcopy(board)
    for i in range(N):
        for j in range(N):
            new_board[j][N - i - 1] = board[i][j]
    return new_board


def convert(lst, N):
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        if new_list[i - 1] == new_list[i]:
            new_list[i - 1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N - len(new_list))


def dfs(N, board, count):
    ret = max([max(i) for i in board])
    if count == 0:
        return ret
    for _ in range(4):
        x = [convert(i, N) for i in board]
        if x != board:
            ret = max(ret, dfs(N, x, count - 1))
        board = rotate90(board, N)
    return ret


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(dfs(N, board, 5))
