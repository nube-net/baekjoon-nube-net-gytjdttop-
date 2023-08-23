import sys
from collections import deque
inputF = sys.stdin.readline

# 입력
n, m, k = map(int, inputF().split())
feed = [list(map(int, inputF().split())) for _ in range(n)]
Farm = [[[5, deque()] for _ in range(n)] for _ in range(n)]  # 깊은 복사

for _ in range(m):
    x, y, z = map(int, inputF().split())
    Farm[x-1][y-1][1].append(z)
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [-1, 1, 0, -1, 1, 0, -1, 1]

for _ in range(k):
    # 사계
    for i in range(n):  # S.S
        for j in range(n):
            # spring
            dead = 0
            for _ in range(len(Farm[i][j][1])):
                tree = Farm[i][j][1].popleft()
                if Farm[i][j][0] >= tree:
                    Farm[i][j][0] -= tree
                    tree += 1
                    Farm[i][j][1].append(tree)
                else:
                    dead += tree//2

            # summer
            Farm[i][j][0] += dead

    for i in range(n):  # F.W
        for j in range(n):
            # fall
            for tree in Farm[i][j][1]:
                if tree%5 == 0:
                    for o in range(8):
                        X, Y = i + dx[o], j + dy[o]
                        if X < 0 or Y < 0 or X >= n or Y >= n:
                            continue
                        Farm[X][Y][1].appendleft(1)

            # winter
            Farm[i][j][0] += feed[i][j]

trees = 0
for i in range(n):
    for j in range(n):
        trees += len(Farm[i][j][1])

print(trees)