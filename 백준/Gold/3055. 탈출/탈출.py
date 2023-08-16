import sys
inputF = sys.stdin.readline

# 입력
r, c = map(int, sys.stdin.readline().split())
Map = [list(map(str, inputF().rstrip())) for _ in range(r)]

# 세팅
Q_water = set()  # 물 우선
Q_location = set()
visited = set()
for i in range(r):
    for j in range(c):
        if Map[i][j] == '.':
            continue
        elif Map[i][j] == '*':
            Q_water.add((i,j))
            visited.add((i, j))
        elif Map[i][j] == 'X':
            visited.add((i,j))
        elif Map[i][j] == 'S':
            Q_location.add((i,j))
            visited.add((i, j))
cnt =0
K = False  # 도착 여부
while Q_water or Q_location:
    cnt += 1
    tmp_w = set()
    tmp_l = set()
    while Q_water:
        x, y = Q_water.pop()

        if x>0:
            if not (x-1,y) in visited:
                if Map[x-1][y] == '.':
                    visited.add((x-1, y))
                    tmp_w.add((x-1,y))
        if x<r-1:
            if not (x+1,y) in visited:
                if Map[x+1][y] == '.':
                    visited.add((x+1, y))
                    tmp_w.add((x+1,y))
        if y>0:
            if not (x,y-1) in visited:
                if Map[x][y-1] == '.':
                    visited.add((x, y-1))
                    tmp_w.add((x,y-1))
        if y<c-1:
            if not (x,y+1) in visited:
                if Map[x][y+1] == '.':
                    visited.add((x, y+1))
                    tmp_w.add((x,y+1))

    while Q_location:
        x, y = Q_location.pop()

        if x>0:
            if not (x-1,y) in visited:
                if Map[x-1][y] == '.':
                    visited.add((x-1, y))
                    tmp_l.add((x-1,y))
                else:
                    K= True
                    break
        if x<r-1:
            if not (x+1,y) in visited:
                if Map[x+1][y] == '.':
                    visited.add((x+1, y))
                    tmp_l.add((x+1,y))
                else:
                    K= True
                    break
        if y>0:
            if not (x,y-1) in visited:
                if Map[x][y-1] == '.':
                    visited.add((x, y-1))
                    tmp_l.add((x,y-1))
                else:
                    K= True
                    break
        if y<c-1:
            if not (x,y+1) in visited:
                if Map[x][y+1] == '.':
                    visited.add((x, y+1))
                    tmp_l.add((x,y+1))
                else:
                    K= True
                    break
    if K:
        break
    Q_water = set(tmp_w)
    Q_location = set(tmp_l)


if K:
    print(cnt)
else:
    print('KAKTUS')