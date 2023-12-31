import sys
inputF = sys.stdin.readline

n, m = map(int, inputF().split())  # 세로, 가로
paper = [list(map(int, inputF().split())) for _ in range(n)]  # 종이 입력
tetris=[[(0, 0), (0, 1), (0, 2), (0, 3)],  # 가로 직선
        [(0, 0), (1, 0), (2, 0), (3, 0)],  # 세로 직선
        [(0, 0), (1, 0), (0, 1), (1, 1)],  # 2*2
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 1), (1, 1), (2, 1), (2, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 0), (0, 1), (1, 0), (2, 0)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 2), (1, 1), (1, 2), (1, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
        [(0, 0), (1, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(0, 1), (1, 1), (1, 0), (2, 0)],
        [(1, 0), (1, 1), (0, 1), (0, 2)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
        [(0, 1), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(0, 0), (1, 0), (1, 1), (2, 0)],
        [(0, 1), (1, 1), (1, 0), (2, 1)]]
result = 0
tmp =0
for x in range(n):
    for y in range(m):
        for case in tetris:
            try:
                tmp=0
                tmp += paper[x + case[0][0]][y + case[0][1]]
                tmp += paper[x + case[1][0]][y + case[1][1]]
                tmp += paper[x + case[2][0]][y + case[2][1]]
                tmp += paper[x + case[3][0]][y + case[3][1]]
                result = max(result, tmp)
            except:
                continue
print(result)