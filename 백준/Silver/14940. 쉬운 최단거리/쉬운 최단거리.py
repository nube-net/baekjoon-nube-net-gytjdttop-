import sys
from collections import deque
inputF = sys.stdin.readline
n, m = map(int, inputF().split())  # n 세로 m 가로

Q = deque()
Map = []
x, y = 0, 0
store = set(i for i in range(n*m))  # (x%m,x//m) -> 좌표, 아직 탐색 안한 좌표들 저장, BFS 반복문 종료 후 존재한 좌표는 -1로 변환

for i in range(n):
    tmp = list(map(int, inputF().split()))
    try:
        x = tmp.index(2)  # 시작 지점 탐색 후 발견 시 저장
        y = i
        Map.append(tmp)
    except:
        Map.append(tmp)
Q.append((x, y))
store.remove(y*m + x)

distance = 0  # 이동 거리
while Q:  # BFS 반복문
    a = len(Q)  # 반복 횟수

    for _ in range(a):
        x, y = Q.popleft()
        Map[y][x] = distance

        if x != 0:  # 좌표 좌 측이 가로 좌측 끝이 아니면
            if (y * m + x - 1) in store:
                if Map[y][x-1] != 0:  # 좌표가 불가능이 아니면
                    Q.append((x-1, y))  # 큐에 추가

                store.remove(y * m + x-1)

        if x != m-1:  # 우 측 탐색
            if (y*m + x+1) in store:
                if Map[y][x + 1] != 0:
                    Q.append((x+1, y))

                store.remove(y * m + x+1)

        if y != 0:  # 상 탐색
            if ((y-1)*m + x) in store:
                if Map[y-1][x] != 0:
                    Q.append((x, y-1))

                store.remove(((y-1) * m + x))

        if y != n-1:  # 하 탐색
            if ((y+1)*m + x) in store:
                if Map[y+1][x] != 0:
                    Q.append((x, y+1))

                store.remove(((y+1) * m + x))
    distance += 1

while store:  # 탐색 못한 좌표들이 존재할 경우
    b = store.pop()
    try:
        if Map[b//m][b%m] != 0:  # 이동 불가능이 아니면
            Map[b//m][b%m] = -1  # -1로 변환
    except:
        continue

for p in Map:
    print(*p)
