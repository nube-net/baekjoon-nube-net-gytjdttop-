import sys
# 트라이 공부중
inputF = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head

        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
        cur.data = string

    def search(self, string):
        cur = self.head
        cnt = 0

        for c in string:
            if c in cur.child:
                cur = cur.child[c]
                if len(cur.child) > 1 or cur.data:  # 문자열 끝이 있거나 분기가 나누어 질 때
                    cnt += 1

        return cnt

while True:
    try:
        trie = Trie()
        n = int(inputF())
        if n == 0:
            break

        a = []
        for _ in range(n):
            tmp = inputF().rstrip()
            trie.insert(tmp)
            a.append(tmp)

        result = 0
        for i in a:
            b = trie.search(i)
            result += b
        print("%.2f" % (result / n))
    except (ValueError, EOFError):
        break
