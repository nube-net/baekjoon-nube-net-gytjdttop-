import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

def char_to_index(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26

C = 52
T = int(input())
for _ in range(T):
    s = input().rstrip()
    t = input().rstrip()
    n = len(s)

    if s == t:
        print(0)
        continue

    arr = [-1] * C
    impossible = False
    for i in range(n):
        a = char_to_index(s[i])
        b = char_to_index(t[i])

        if arr[a] != -1 and arr[a] != b:
            print(-1)
            impossible = True
            break
        arr[a] = b

    if impossible:
        continue

    tmp = list(range(C))
    mapped = sorted(x if x != -1 else -1 for x in arr)
    if mapped == tmp:
        print(-1)
        continue

    parent = list(tmp)
    cnt = [0] * C
    ans = 0

    for i in range(C):
        if arr[i] != -1 and arr[i] != i:
            cnt[arr[i]] += 1
            union(i, arr[i])
            ans += 1

    groups = {}
    for i in range(C):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    for group in groups.values():
        if len(group) > 1 and all(cnt[i] == 1 for i in group):
            ans += 1

    print(ans)
