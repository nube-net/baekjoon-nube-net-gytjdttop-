import sys
inputF = sys.stdin.readline
# 트리 공부 중

class Node:
    def __init__(self, item, left=None, right=None):
        self.data = item
        self.left = left
        self.right = right


def pre_order(node):  # 전위 순회
    print(node.data, end="")
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])


def in_order(node):  # 중위 순회
    if node.left != '.':
        in_order(tree[node.left])
    print(node.data, end="")
    if node.right != '.':
        in_order(tree[node.right])


def post_order(node):  # 후위 순회
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.data, end="")


n = int(inputF())  # 노드의 수
tree = {}

for _ in range(n):
    data, left, right = inputF().split()
    tree[data] = Node(data, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])


