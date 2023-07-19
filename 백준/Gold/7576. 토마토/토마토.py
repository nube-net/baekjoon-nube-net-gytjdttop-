import sys
from collections import deque


inputF = sys.stdin.readline
Q = deque()  # 큐 생성
Map = set()  # 익은 토마토 위치 저장

m, n = map(int, inputF().split())  # m 가로 칸수 n 세로 칸수

box = []  # 토마토 상자
for _ in range(n):
    tmp0 = list(map(int, inputF().split()))
    for o in range(m):
        if tmp0[o] == 1:
            Map.add((_, o))  # _번째 줄 o번째 칸
    box.append(tmp0)

c=0
while True:
    Map1 = set()
    while Map:
        x, y = Map.pop()  # x번째 줄 y번째 칸

        # 상
        if x != 0:
            if box[x - 1][y] == 0:
                box[x - 1][y] = c + 1
                Map1.add((x - 1, y))

        # 하
        if x != n - 1:
            if box[x + 1][y] == 0:
                box[x + 1][y] = c + 1
                Map1.add((x + 1, y))

        # 좌
        if y != 0:
            if box[x][y - 1] == 0:
                box[x][y - 1] = c + 1
                Map1.add((x, y - 1))

        # 우
        if y != m - 1:
            if box[x][y + 1] == 0:
                box[x][y + 1] = c + 1
                Map1.add((x, y + 1))
    Map.update(Map1)
    if Map1:
        c += 1
    else:
        break


key = False  # 익지 않은 토마토 여부
for _ in box:
    aa = set(_)
    if 0 in aa:
        key = True

if key:
    print(-1)
else:
    print(c)
