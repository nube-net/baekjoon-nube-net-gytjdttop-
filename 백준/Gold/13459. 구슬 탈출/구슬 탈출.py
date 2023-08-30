import sys
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
Map = [list(input().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if Map[i][j] == 'R':
            red = [i, j]
        elif Map[i][j] == 'B':
            blue = [i, j]
Q = deque()
Q.append(tuple(red+blue))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1
check = set()
ans =False
while cnt < 11:
    l = len(Q)
    for _ in range(l):
        loc = Q.popleft()
        check.add(loc)
        R = [loc[0], loc[1]]
        B = [loc[2], loc[3]]
        for i in range(4):
            goal_b = False
            goal_r = False
            r = copy.deepcopy(R)
            b = copy.deepcopy(B)
            key_r, key_b = True, True
            tmp = set()  # 먼저 멈춘 구슬 위치
            if (R[0]+dx[i], R[1]+dy[i]) == tuple(B):  # 바로 옆에 파란 구슬 있을 경우, 파란 구슬 먼저 이동
                while key_r or key_b:
                    if key_b:
                        if (b[0] + dx[i], b[1] + dy[i]) in tmp:
                            key_b = False
                        if Map[b[0] + dx[i]][b[1] + dy[i]] == '#':
                            key_b = False
                            tmp.add(tuple(b))
                        elif Map[b[0] + dx[i]][b[1] + dy[i]] == 'O':
                            goal_b = True
                            key_b = False
                        if key_b:
                            b[0] += dx[i]
                            b[1] += dy[i]
                    if key_r:
                        if (r[0] + dx[i], r[1] + dy[i]) in tmp:
                            key_r = False
                        if Map[r[0] + dx[i]][r[1] + dy[i]] == '#':
                            key_r = False
                            tmp.add(tuple(r))
                        elif Map[r[0] + dx[i]][r[1] + dy[i]] == 'O':
                            goal_r = True
                            key_r = False
                        if key_r:
                            r[0] += dx[i]
                            r[1] += dy[i]
                if goal_b:
                    continue
                elif goal_r:
                    ans = True
                    break
                else:
                    if tuple(r + b) not in check:
                        Q.append(tuple(r + b))
            else:
                while key_r or key_b:
                    if key_r:
                        if (r[0] + dx[i], r[1] + dy[i]) in tmp:
                            key_r = False
                        if Map[r[0] + dx[i]][r[1] + dy[i]] == '#':
                            key_r = False
                            tmp.add(tuple(r))
                        elif Map[r[0] + dx[i]][r[1] + dy[i]] == 'O':
                            goal_r = True
                            key_r = False
                        if key_r:
                            r[0] += dx[i]
                            r[1] += dy[i]
                    if key_b:
                        if (b[0] + dx[i], b[1] + dy[i]) in tmp:
                            key_b = False
                        if Map[b[0] + dx[i]][b[1] + dy[i]] == '#':
                            key_b = False
                            tmp.add(tuple(b))
                        elif Map[b[0] + dx[i]][b[1] + dy[i]] == 'O':
                            goal_b = True
                            key_b = False
                        if key_b:
                            b[0] += dx[i]
                            b[1] += dy[i]
                if goal_b:
                    continue
                elif goal_r:
                    ans = True
                    break
                else:
                    if tuple(r + b) not in check:
                        Q.append(tuple(r + b))
        if ans:
            break
    if ans:
        break
    cnt +=1

if cnt >10:
    print(0)
else:
    print(1)
