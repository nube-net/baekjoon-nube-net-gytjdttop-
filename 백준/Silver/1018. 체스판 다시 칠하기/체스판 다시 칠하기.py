def code(a):
    c = 0
    for o in range(8):
        for p in range(8):
            if (o+p) % 2 == 0:
                if a[o][p] == 'W':
                    c += 1
            else:
                if a[o][p] == 'B':
                    c += 1
    return min(c, 64 - c)

N, M = map(int, input().split())  # N 세로 M 가로

tmp = []  # 원본
for i in range(N):
    tmp.append(input().rstrip())

result = float('inf')

for x in range(M - 7):
    for y in range(N - 7):
        board = []
        for i in range(y, y + 8):
            board.append(tmp[i][x:x + 8])
        result = min(result, code(board))

print(result)
