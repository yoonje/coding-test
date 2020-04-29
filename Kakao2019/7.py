def get_possible_block(board, i, j):
    try:
        if (board[i + 1][j] == board[i][j] and
                board[i + 1][j + 1] == board[i][j] and
                board[i + 1][j + 2] == board[i][j]):
            return (i, j + 1), (i, j + 2), board[i][j]
    except:
        pass
    try:
        if (board[i + 1][j] == board[i][j] and
                board[i + 2][j] == board[i][j] and
                board[i + 2][j - 1] == board[i][j]):
            return (i, j - 1), (i + 1, j - 1), board[i][j]
    except:
        pass
    try:
        if (board[i + 1][j] == board[i][j] and
                board[i + 2][j] == board[i][j] and
                board[i + 2][j + 1] == board[i][j]):
            return (i, j + 1), (i + 1, j + 1), board[i][j]
    except:
        pass
    try:
        if (board[i + 1][j] == board[i][j] and
                board[i + 1][j - 1] == board[i][j] and
                board[i + 1][j - 2] == board[i][j]):
            return (i, j - 1), (i, j - 2), board[i][j]
    except:
        pass
    try:
        if (board[i + 1][j - 1] == board[i][j] and
                board[i + 1][j] == board[i][j] and
                board[i + 1][j + 1] == board[i][j]):
            return (i, j - 1), (i, j + 1), board[i][j]
    except:
        pass
    return None


def preprocess(board):
    checked = set()
    list = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0 and board[i][j] not in checked:
                checked.add(board[i][j])
                type = get_possible_block(board, i, j)
                if type is not None:
                    list.append(type)
    return list


def over_head(board, i, j):
    for a in range(i + 1):
        if board[a][j] != 0:
            return True
    return False


def remove(board, k):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == k:
                board[i][j] = 0


def solution(board):
    answer = 0
    removed = set()
    list = preprocess(board)  # 지워질 가능성이 있는 블럭만 남기기
    while True:
        check = False
        for i in list:
            a1, b1 = i[0]
            a2, b2 = i[1]
            k = i[2]
            if k in removed:  # 이미 지워진 블럭이면 무시
                continue
            # 남은 두 공간의 위에 아무 블럭도 없다면 해당 블럭 지움 처리
            if not over_head(board, a1, b1) and not over_head(board, a2, b2):
                removed.add(k)
                remove(board, k)
                check = True
                answer += 1
        if check is False:
            break
    return answer
