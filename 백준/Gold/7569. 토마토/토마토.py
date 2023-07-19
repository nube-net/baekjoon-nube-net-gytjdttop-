import sys
inputF = sys.stdin.readline

Map = set()  # 익은 토마토 위치 저장
m, n, h = map(int, inputF().split())  # m 가로 칸수 n 세로 칸수 h 층 수

boxes = []
for j in range(h):
    box = []  # 토마토 상자
    for _ in range(n):
        tmp0 = list(map(int, inputF().split()))
        for o in range(m):
            if tmp0[o] == 1:
                Map.add((j, _, o))  # j번째 상자 _번째 줄 o번째 칸
        box.append(tmp0)
    boxes.append(box)


c=0
while True:
    Map1 = set()
    while Map:
        z, x, y = Map.pop()  # z번째 상자 x번째 줄 y번째 칸

        # 상
        if x != 0:
            if boxes[z][x - 1][y] == 0:
                boxes[z][x - 1][y] = c + 1
                Map1.add((z,x - 1, y))

        # 하
        if x != n - 1:
            if boxes[z][x + 1][y] == 0:
                boxes[z][x + 1][y] = c + 1
                Map1.add((z,x + 1, y))

        # 좌
        if y != 0:
            if boxes[z][x][y - 1] == 0:
                boxes[z][x][y - 1] = c + 1
                Map1.add((z,x, y - 1))

        # 우
        if y != m - 1:
            if boxes[z][x][y + 1] == 0:
                boxes[z][x][y + 1] = c + 1
                Map1.add((z,x, y + 1))

        # 위층 상자
        if z != 0:
            if boxes[z-1][x][y] == 0:
                boxes[z-1][x][y] = c + 1
                Map1.add((z-1, x, y))

        # 아래층 상자
        if z != h-1:
            if boxes[z+1][x][y] == 0:
                boxes[z+1][x][y] = c + 1
                Map1.add((z+1, x, y))
    Map.update(Map1)
    if Map1:
        c += 1
    else:
        break


key = False  # 익지 않은 토마토 여부
for box_ in boxes:
    for _ in box_:
        aa = set(_)
        if 0 in aa:
            key = True

if key:
    print(-1)
else:
    print(c)
