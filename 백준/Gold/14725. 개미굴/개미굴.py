import sys
inputF = sys.stdin.readline
# 트라이 공부중
class Node(object):
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):  # 이번 문제에서는 리스트로 입력됨
        cur = self.head
        cur.count += 1

        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.count += 1

    def display(self, node=None, indent=0):
        if node is None:
            node = self.head

        # 현재 노드 출력
        if node.data is not None:
            print('-' * (indent-2) + node.data)

        # 자식 노드 출력 (재귀)
        for child in node.child.values():
            self.display(child, indent + 2)

    # 미사용된 함수들

    def count(self, prefix):
        cur = self.head

        for c in prefix:
            if c not in cur.child:
                return 0
            cur = cur.child[c]

        return cur.count

    def search(self, string):
        cur = self.head

        for c in string:
            if c in cur.child:
                cur = cur.child[c]
            else:
                return False

        if cur.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        cur = self.head
        words = []

        for p in prefix:
            if p in cur.child:
                cur = cur.child[p]
            else:
                return None

        cur = [cur]

        next_ = []
        while True:
            for node in cur:
                if node.data:
                    words.append(node.data)
                next_.extend(list(node.child.values()))

            if len(next_) != 0:
                cur = next
                next_ = []
            else:
                break

        return words

trie = Trie()
n = int(inputF())
tmp = []
for _ in range(n):
    A = list(map(str, inputF().split()))
    tmp.append(A[1:])
tmp.sort()

for _ in tmp:
    trie.insert(_)

trie.display()

