class Node(object):
    def __init__(self, x=0, y=0, x2=1, y2=0, dist=0, state=True):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.dist = dist  # 로봇이 이동한 거리
        self.state = state  # 로봇 가로 = True, 세로 = False

    def getXY(self):
        return self.x, self.y

    def getXY2(self):
        return self.x2, self.y2


def find_next(board, node_):
    N = len(board) - 1
    nextDest = []
    x, y = node_.getXY()
    x2, y2 = node_.getXY2()
    dist = node_.dist + 1

    if node_.state:  # 가로
        if x2 < N and board[y][x2 + 1] == 0:  # 로봇의 오른쪽 블럭이 이동 가능한 곳
            nextDest.append(Node(x + 1, y, x2 + 1, y2, dist, True))  # 1 오른쪽
        if x > 0 and board[y][x - 1] == 0:  # 로봇의 왼쪽 블럭이 이동 가능한 곳
            nextDest.append(Node(x - 1, y, x2 - 1, y2, dist, True))  # 2 왼쪽
        if y2 < N and board[y2 + 1][x] == 0 and board[y + 1][x + 1] == 0:  # 로봇의 아래쪽 블럭 2개가 이동 가능한 곳
            nextDest.append(Node(x, y + 1, x + 1, y + 1, dist, True))  # 3 아래로
            nextDest.append(Node(x, y, x, y + 1, dist, False))  # 4 회전1
            nextDest.append(Node(x + 1, y, x + 1, y + 1, dist, False))  # 5 회전 2
        if y > 0 and board[y - 1][x] == 0 and board[y - 1][x + 1] == 0:  # 로봇의 위쪽 블럭 2개가 이동 가능한 곳
            nextDest.append(Node(x, y - 1, x2, y2 - 1, dist, True))  # 6 위로
            nextDest.append(Node(x, y - 1, x, y, dist, False))  # 7 회전 3
            nextDest.append(Node(x + 1, y - 1, x2, y2, dist, False))  # 8 회전 4
    else:  # 세로
        if y2 < N and board[y2 + 1][x] == 0:  # 로봇의 아래쪽 블럭이 이동 가능한 곳
            nextDest.append(Node(x, y + 1, x2, y2 + 1, dist, False))  # 1
        if y > 0 and board[y - 1][x] == 0:  # 로봇의 위쪽 블럭이 이동 가능한 곳
            nextDest.append(Node(x, y - 1, x2, y2 - 1, dist, False))  # 2
        if x2 < N and board[y][x2 + 1] == 0 and board[y + 1][x2 + 1] == 0:  # 로봇의 오른쪽 블럭 2개가 이동 가능한 곳
            nextDest.append(Node(x + 1, y, x2 + 1, y2, dist, False))  # 3
            nextDest.append(Node(x, y, x2 + 1, y2 - 1, dist, True))  # 4
            nextDest.append(Node(x2, y2, x + 1, y + 1, dist, True))  # 5
        if x > 0 and board[y][x - 1] == 0 and board[y + 1][x - 1] == 0:  # 로봇의 왼쪽 블럭 2개가 이동 가능한 곳
            nextDest.append(Node(x - 1, y, x2 - 1, y2, dist, False))  # 6
            nextDest.append(Node(x - 1, y, x2, y2 - 1, dist, True))  # 7
            nextDest.append(Node(x - 1, y + 1, x2, y2, dist, True))  # 8

    return nextDest


def solution(board):
    answer = 0
    N = len(board) - 1
    curNode = Node()
    queue = [curNode]
    visit = []  # 방문한 블럭 저장

    while queue:
        curNode = queue.pop(0)
        if curNode.getXY() == (N, N) or curNode.getXY2() == (N, N):
            return curNode.dist
        if (curNode.getXY(), curNode.getXY2()) not in visit:  # 이미 방문한 블럭인지 확인
            visit.append((curNode.getXY(), curNode.getXY2()))
            queue.extend(find_next(board, curNode))

    return answer
