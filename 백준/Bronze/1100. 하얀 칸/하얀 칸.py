import sys
inputF = sys.stdin.readline

Map = [list(inputF().rstrip()) for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            if Map[i][j] == 'F':
                cnt += 1

print(cnt)