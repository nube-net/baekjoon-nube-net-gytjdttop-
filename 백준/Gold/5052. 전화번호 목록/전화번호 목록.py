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

    def insert(self, string):
        cur = self.head
        cur.count += 1

        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.count += 1

    def count(self, prefix):
        cur = self.head

        for c in prefix:
            if c not in cur.child:
                return 0
            cur = cur.child[c]

        return cur.count

T = int(inputF())
for _ in range(T):
    n = int(inputF())
    trie = Trie()
    S = []
    for __ in range(n):
        tmp = inputF().rstrip()
        S.append(tmp)
        trie.insert(tmp)

    S.sort()

    result = "YES"
    for i in S:
        if trie.count(i) > 1:
            result = "NO"
            break
    print(result)