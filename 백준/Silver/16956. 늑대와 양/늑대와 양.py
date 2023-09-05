import sys
import copy
input = sys.stdin.readline

r, c = map(int, input().split())
Map = [list(input().rstrip()) for _ in range(r)]
sheep = False
wolf = False
dx = [1, -1 ,0 ,0]
dy = [0, 0, 1, -1]
for i in range(r):
    for j in range(c):
        if Map[i][j] == '.':
            Map[i][j] = 'D'
        elif Map[i][j] == 'S':
            if not sheep:
                sheep = True

            for _ in range(4):
                x = i+dx[_]
                y = j+dy[_]
                if x < 0 or y < 0 or x >= r or y >= c:
                    continue
                if Map[x][y] == 'W':
                    print(0)
                    exit()
        else:
            if not wolf:
                wolf = True

print(1)
for p in Map:
    print(''.join(p))