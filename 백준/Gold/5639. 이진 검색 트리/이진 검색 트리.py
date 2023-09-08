import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, item, parent=None, left=None, right=None):
        self.data = item
        self.parent = parent
        self.left = left
        self.right = right


def post_order(node):
    if node.left:
        post_order(tree[node.left])
    if node.right:
        post_order(tree[node.right])
    print(node.data)


tree = {}
root = None
while True:
    try:
        a = int(input().strip())

        if not root:
            root = a
            tree[a] = Node(a)
            cur = a
            continue

        tmp = root
        parent = None
        while tmp:
            if a < tmp:
                parent = tmp
                tmp = tree[tmp].left
            else:
                parent = tmp
                tmp = tree[tmp].right

        tree[a] = Node(a, parent)
        if a < parent:
            tree[parent].left = a
        else:
            tree[parent].right = a

    except:
        break

post_order(tree[root])
