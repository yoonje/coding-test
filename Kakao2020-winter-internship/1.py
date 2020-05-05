def move_item(board, move):
    for i in range(len(board)):
        if board[i][move] != 0:
            item = board[i][move]
            board[i][move] = 0
            return item
    return None


def remove_sequence_items(moved_list):
    for i in range(1, len(moved_list)):
        if moved_list[i - 1] == moved_list[i]:
            return moved_list[:i - 1] + moved_list[i + 1:]
    return False


def solution(board, moves):
    moved_list = list()
    for move in moves:
        moved_list.append(move_item(board, move - 1))
    while True:
        try:
            moved_list.index(None)
            moved_list.remove(None)
        except ValueError:
            break
    cnt = 0
    while True:
        moved_list = remove_sequence_items(moved_list)
        if moved_list is not False:
            cnt += 2
        else:
            return cnt

