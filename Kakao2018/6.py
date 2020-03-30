dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]


def safe(width, height, c_idx, r_idx):
    for x, y in zip(dx, dy):
        if width - 1 < x + c_idx or x + c_idx < 0 or height - 1 < y + r_idx or y + r_idx < 0:
            return False
    return True


def del_check(board, c_idx, r_idx):
    square_set = set()
    for x, y in zip(dx, dy):
        square_set.add(board[y + r_idx][x + c_idx])
    if len(square_set) == 1 and square_set != {" "}:
        return True
    return False


def del_block(board, c_idx, r_idx):
    for x, y in zip(dx, dy):
        board[y + r_idx][x + c_idx] = ""
    return board


def total_del_block(board):
    total = 0
    for row in board:
        for block in row:
            if block == ' ':
                total += 1
    return total


def drop_block(width, height, board):
    for x_idx in range(width):
        tmp_lst = []
        for y_idx in range(height):
            tmp_lst.append(board[y_idx][x_idx])
        col_str = "".join(tmp_lst)
        col_str = (height - len(col_str)) * " " + col_str
        for y_idx in range(height):
            board[y_idx][x_idx] = col_str[y_idx]
    return board


def solution(height, width, board):
    board = [[block for block in row] for row in board]
    answer = 0
    while True:
        del_lst = []
        for r_idx in range(height):
            for c_idx in range(width):
                if safe(width, height, c_idx, r_idx):
                    if del_check(board, c_idx, r_idx):
                        del_lst.append([c_idx, r_idx])
        if len(del_lst) == 0:
            break
        for del_pos in del_lst:
            board = del_block(board, del_pos[0], del_pos[1])
        board = drop_block(width, height, board)
    return total_del_block(board)
