import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, x, id, left_bound, right_bound):
        self.x = x
        self.id = id
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.left_node = None
        self.right_node = None


preorder_result = []
postorder_result = []


def preorder(node):
    preorder_result.append(node.id)
    if node.left_node is not None:
        preorder(node.left_node)
    if node.right_node is not None:
        preorder(node.right_node)


def postorder(node):
    if node.left_node is not None:
        postorder(node.left_node)
    if node.right_node is not None:
        postorder(node.right_node)
    postorder_result.append(node.id)


def solution(nodeinfo):
    nodeinfo = [i + [idx + 1] for idx, i in enumerate(nodeinfo)]  # 세 번째 원소로 인덱스 넣기
    nodeinfo = sorted(nodeinfo, key=lambda x: x[1], reverse=True)  # Y 좌표를 기준으로 내림차순 정렬
    array = []  # 같은 Y 좌표에 여러 개의 X 좌표가 들어가도록 리스트 구성
    now = -1
    for i in nodeinfo:
        y = i[1]
        if y != now:
            array.append([])
            now = y
        array[len(array) - 1].append((i[0], i[2]))  # X 값과 인덱스만 삽입
    for i in range(len(array)):
        array[i] = sorted(array[i])
    root = Node(array[0][0][0], array[0][0][1], 0, 100000)  # X 루트 노드 설정
    node_list = [[]]
    node_list[0].append(root)
    for level in range(1, len(array)):  # 두 번째 Level 차례대로 확인
        node_list.append([])
        for data in array[level]:
            x = data[0]
            id = data[1]
            for parent_node in node_list[level - 1]:
                if parent_node.left_bound <= x and parent_node.x > x:
                    now_node = Node(x, id, parent_node.left_bound, parent_node.x)
                    parent_node.left_node = now_node
                    node_list[level].append(now_node)
                    break
                elif parent_node.right_bound >= x and parent_node.x < x:
                    now_node = Node(x, id, parent_node.x, parent_node.right_bound)
                    parent_node.right_node = now_node
                    node_list[level].append(now_node)
                    break
    preorder(root)
    postorder(root)
    return [preorder_result, postorder_result]
