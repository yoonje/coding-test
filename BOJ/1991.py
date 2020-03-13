from collections import deque


def inorder(tree, index=1):
    if tree[index] and tree[index] != ".":
        inorder(tree, index * 2)
        print(tree[index], end="")
        inorder(tree, index * 2 + 1)


def preorder(tree, index=1):
    if tree[index] and tree[index] != ".":
        print(tree[index], end="")
        preorder(tree, index * 2)
        preorder(tree, index * 2 + 1)


def postorder(tree, index=1):
    if tree[index] and tree[index] != ".":
        postorder(tree, index * 2)
        postorder(tree, index * 2 + 1)
        print(tree[index], end="")


node_num = int(input())

array_tree = [None] * 1000

data_deque = deque()

for _ in range(node_num):
    value, left, right = list(input().split(" "))
    data_deque.append((value, left, right))

while data_deque:
    value, left, right = data_deque.popleft()
    if value == "A":
        array_tree[1] = value
        array_tree[2] = left
        array_tree[3] = right
    else:
        if value in array_tree:
            array_tree[array_tree.index(value) * 2] = left
            array_tree[array_tree.index(value) * 2 + 1] = right
        else:
            data_deque.append((value, left, right))

preorder(array_tree)
print("")
inorder(array_tree)
print("")
postorder(array_tree)