import sys
stack = []  # 스택

n = int(sys.stdin.readline())  # 입력

Map = set([i for i in range(n*n)])  # 탐색 미완료 위치, x번째 줄 y 번째 칸 -> x*n + y 숫자
Map1 = set(Map)  # 색약
block = []
for _ in range(n):
    tmp0 = sys.stdin.readline().rstrip()
    block.append(list(tmp0))
block1 = list(block)  # 색약
a = 0  # 일반
b = 0  # 적록 색약
# 일반 기준
while Map:  # 모든 좌표 탐색할 때까지
    tmp1=Map.pop()
    stack.append((tmp1//n, tmp1%n))
    a += 1
    tmp = block[tmp1//n][tmp1%n]
    while stack:  # 현재 구역
        x, y = stack.pop()

        # 상
        if x != 0:
            if (x-1)*n + y in Map:
                if block[x-1][y] == tmp:
                    stack.append((x-1, y))
                    Map.remove((x-1)*n + y)

        # 하
        if x != n-1:
            if (x+1)*n+y in Map:
                if block[x+1][y] == tmp:
                    stack.append((x+1, y))
                    Map.remove((x+1)*n+y)

        # 좌
        if y != 0:
            if x*n + (y-1) in Map:
                if block[x][y-1] == tmp:
                    stack.append((x, y-1))
                    Map.remove(x*n + (y-1))

        # 우
        if y != n-1:
            if x*n+ (y+1) in Map:
                if block[x][y+1] == tmp:
                    stack.append((x, y+1))
                    Map.remove(x*n+ (y+1))
# 색약 기준
while Map1:  # 모든 좌표 탐색할 때까지
    tmp1 = Map1.pop()
    stack.append((tmp1//n, tmp1%n))
    b += 1
    tmp = block1[tmp1//n][tmp1%n]
    if tmp == 'B':
        bb = {'B'}
    else:
        bb = {'R','G'}
    while stack:  # 현재 구역
        x, y = stack.pop()

        # 상
        if x != 0:
            if (x-1)*n + y in Map1:
                if block1[x-1][y] in bb:
                    stack.append((x-1, y))
                    Map1.remove((x-1)*n + y)

        # 하
        if x != n-1:
            if (x+1)*n+y in Map1:
                if block1[x+1][y] in bb:
                    stack.append((x+1, y))
                    Map1.remove((x+1)*n+y)

        # 좌
        if y != 0:
            if x*n + (y-1) in Map1:
                if block1[x][y-1]in bb:
                    stack.append((x, y-1))
                    Map1.remove(x*n + (y-1))

        # 우
        if y != n-1:
            if x*n+ (y+1) in Map1:
                if block1[x][y+1] in bb:
                    stack.append((x, y+1))
                    Map1.remove(x*n+ (y+1))

print(f"{a} {b}")