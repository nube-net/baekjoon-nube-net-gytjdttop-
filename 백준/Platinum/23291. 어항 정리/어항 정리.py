import sys
from collections import  deque
input = sys.stdin.readline

n, K = map(int, input().split())
a = deque(map(int, input().split()))
q =deque()
q.append(a)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
while max(q[0])-min(q[0]) > K:
    cnt += 1
    # 물고기 한마리 넣기
    idx = []
    val = 10001
    for i in range(len(q[0])):
        if q[0][i] > val:
            continue
        elif q[0][i] == val:
            idx.append(i)
        else:
            val = q[0][i]
            idx = [i]
    for index in idx:
        q[0][index] += 1


    # 1개 쌓기
    q0 = deque([q[0].popleft()])
    q.appendleft(q0)

    # 공중 부양 반복
    while True:
        h = len(q)
        tmp = len(q[-1])-len(q[0])
        if tmp < h:
            break
        Q = deque()
        for _ in range(len(q[0])):
            q0 = deque()
            for i in range(h):
                q0.appendleft(q[i].popleft())
            Q.append(q0)
        Q.append(q.pop())
        q = deque(Q)
        #print(q)

    # 물고기 수 조절
    S = set() # 받을 물고기 저장
    h = len(q)
    for i in range(h):
        l  = len(q[i])
        for j in range(l):
            cur = int(q[i][j])
            for k in range(4):
                if k ==0 and j>=len(q[0]) and i == h-1:
                    continue
                x,y = i+dx[k],j+dy[k]
                if x <0 or x >=h or y<0 or y>=l:
                    continue
                if cur < q[x][y]:
                    d = (q[x][y]-cur)//5
                    if d>0:
                        S.add((i,j,x,y,d))
                        #print(i,j,x,y,d)
    while S:
        i,j,x,y,val = S.pop()
        q[x][y] -= val
        q[i][j] += val

    # 일렬로 놓기
    Q = deque()
    for _ in range(len(q[-1])):
        for i in range(h-1,-1,-1):
            if q[i]:
                Q.append(q[i].popleft())

    # 공중 부양 2차
    q0 = deque()
    for _ in range(n//2):
        q0.appendleft(Q.popleft())
    q = deque()
    q.append(q0)
    q.append(Q)
    q0, Q = deque(),deque()
    for _ in range(n//4):
        q0.appendleft(q[1].popleft())
        Q.appendleft(q[0].popleft())
    q.appendleft(Q)
    q.appendleft(q0)
    #print(q)

    # 물고기 수 조절 2차
    S = set()  # 받을 물고기 저장
    h = len(q)
    for i in range(h):
        l = len(q[i])
        for j in range(l):
            cur = int(q[i][j])
            for k in range(4):
                if k == 0 and j >= len(q[0]) and i == h - 1:
                    continue
                x, y = i + dx[k], j + dy[k]
                if x < 0 or x >= h or y < 0 or y >= l:
                    continue
                if cur < q[x][y]:
                    d = (q[x][y] - cur) // 5
                    if d > 0:
                        S.add((i, j, x, y, d))
                        # print(i,j,x,y,d)
    while S:
        i, j, x, y, val = S.pop()
        q[x][y] -= val
        q[i][j] += val
    #print(q)
    # 일렬로 놓기
    Q = deque()
    for _ in range(len(q[-1])):
        for i in range(h - 1, -1, -1):
            if q[i]:
                Q.append(q[i].popleft())
    #print(Q)
    q = deque()
    q.append(Q)
    #print(q)
print(cnt)