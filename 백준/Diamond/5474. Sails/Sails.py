import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# 레드블랙트리 자료구조 참고하였습니다.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.color = 'R'
        self.left = None
        self.right = None
        self.parent = None


class TreeSet:
    def __init__(self):
        self.TNULL = TreeNode(0)
        self.TNULL.color = 'B'
        self.root = self.TNULL
    
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def insert_fixup(self, k):
        while k.parent.color == 'R':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.rotate_left(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'B'
    
    def insert(self, key):
        node = TreeNode(key)
        node.parent = None
        node.key = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'R'
        
        y = None
        x = self.root
        
        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        
        if node.parent is None:
            node.color = 'B'
            return
        
        if node.parent.parent is None:
            return
        
        self.insert_fixup(node)
    
    def delete_fixup(self, x):
        while x != self.root and x.color == 'B':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'R':
                    s.color = 'B'
                    x.parent.color = 'R'
                    self.rotate_left(x.parent)
                    s = x.parent.right
                if s.left.color == 'B' and s.right.color == 'B':
                    s.color = 'R'
                    x = x.parent
                else:
                    if s.right.color == 'B':
                        s.left.color = 'B'
                        s.color = 'R'
                        self.rotate_right(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 'B'
                    s.right.color = 'B'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'R':
                    s.color = 'B'
                    x.parent.color = 'R'
                    self.rotate_right(x.parent)
                    s = x.parent.left
                if s.right.color == 'B' and s.left.color == 'B':
                    s.color = 'R'
                    x = x.parent
                else:
                    if s.left.color == 'B':
                        s.right.color = 'B'
                        s.color = 'R'
                        self.rotate_left(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 'B'
                    s.left.color = 'B'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'B'
    
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def delete(self, key):
        z = self.root
        while z != self.TNULL:
            if z.key == key:
                break
            if key < z.key:
                z = z.left
            else:
                z = z.right
        
        if z == self.TNULL:
            return
        
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == 'B':
            self.delete_fixup(x)
    
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
    
    def in_order_traversal(self, node, result):
        if node != self.TNULL:
            self.in_order_traversal(node.left, result)
            result.append(node.key)
            self.in_order_traversal(node.right, result)
    
    def to_list(self):
        result = []
        self.in_order_traversal(self.root, result)
        return result
    
    def find_max_less_than(self, x):
        node = self.root
        best = None
        
        while node != self.TNULL:
            if node.key < x:
                best = node.key
                node = node.right
            else:
                node = node.left
        
        return best
    
    def find_min_more_than(self, x):
        node = self.root
        best = None
        
        while node != self.TNULL:
            if node.key > x:
                best = node.key
                node = node.left
            else:
                node = node.right
        
        return best


class FastNegativeIndexTracker:
    def __init__(self, arr):
        self.arr = arr[:]
        self.negative_tree = TreeSet()
        for i, val in enumerate(arr):
            if val < 0:
                self.negative_tree.insert(i)
    
    def update(self, index, delta):
        prev_value = self.arr[index]
        new_value = prev_value + delta
        if prev_value < 0:
            self.negative_tree.delete(index)
        self.arr[index] = new_value
        if new_value < 0:
            self.negative_tree.insert(index)
    
    def get_negative_indices(self):
        return self.negative_tree.to_list()
    
    def get_max_negative_index_less_than(self, x):
        return self.negative_tree.find_max_less_than(x)
    
    def get_min_negative_index_more_than(self, x):
        return self.negative_tree.find_min_more_than(x)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()
s = set()
s.add(1)
dp = [0 for _ in range(a[-1][0] + 2)]
dp[1] = -1
tracker = FastNegativeIndexTracker(dp)
for h, c in a:
    H = h
    mid = tracker.get_max_negative_index_less_than(h + 1)
    if mid == None:
        mid = 1
    
    if h - mid + 1 >= c:
        tracker.update(mid, 1)
        tracker.update(mid + c, -1)
    else:
        mid = tracker.get_min_negative_index_more_than(h - c)
        if mid == None:
            mid = 1
        if True:
            tracker.update(mid, 1)
            tracker.update(h + 1, -1)
            val = c - (h + 1 - mid)
            if val > 0:
                mid2 = tracker.get_max_negative_index_less_than(h - c + 1)
                if mid2 == None:
                    mid2 = 1
                tracker.update(mid2, 1)
                tracker.update(mid2 + val, -1)

dp = tracker.arr
dp[0] = 1
for i in range(1, len(dp)):
    dp[i] = dp[i - 1] + dp[i]
ans = 0
for i in range(1, len(dp)):
    ans += dp[i] * (dp[i] - 1) // 2
print(ans)
