import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
v = [[[[1000 for _ in range(m)] for _ in range(n)] for _ in range(1 << m)] for _ in range(1 << n)]
mp = [[[list(r) for r in arr] for _ in range(1 << m)] for _ in range(1 << n)]

for rb in range(1 << n):
    rb_lst = [i for i in range(n) if rb & (1 << i)]
    for cb in range(1 << m):
        cb_lst = [i for i in range(m) if cb & (1 << i)]
        for r in rb_lst:
            for c in range(m):
                mp[rb][cb][r][c] = 'D' if mp[rb][cb][r][c] == 'C' else 'C' if mp[rb][cb][r][c] == 'D' else mp[rb][cb][r][c]
        for c in cb_lst:
            for r in range(n):
                mp[rb][cb][r][c] = 'D' if mp[rb][cb][r][c] == 'C' else 'C' if mp[rb][cb][r][c] == 'D' else mp[rb][cb][r][c]

q = deque([(0, 0, 0, 0, 0)])
v[0][0][0][0] = 0
flag = True
while q:
    t, r, c, rb, cb = q.popleft()
    if r == n-1 and c == m-1:
        print(t)
        flag = False
        break

    nt = t + 1
    nrb = rb ^ (1 << r)
    ncb = cb ^ (1 << c)

    if v[nrb][ncb][r][c] > nt:
        v[nrb][ncb][r][c] = nt
        q.append((nt, r, c, nrb, ncb))

    for cr, cc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nr, nc = r + cr, c + cc
        if 0 <= nr < n and 0 <= nc < m:
            trn = int((rb & (1 << r)) != (cb & (1 << c)))
            if ((cr == 0 and (mp[rb][cb][r][c] in "DA") and (mp[rb][cb][nr][nc] in "DA")) or (cr != 0 and (mp[rb][cb][r][c] in "CA") and (mp[rb][cb][nr][nc] in "CA"))):
                if v[rb][cb][nr][nc] > nt:
                    v[rb][cb][nr][nc] = nt
                    q.append((nt, nr, nc, rb, cb))
if flag:
    print(-1)
