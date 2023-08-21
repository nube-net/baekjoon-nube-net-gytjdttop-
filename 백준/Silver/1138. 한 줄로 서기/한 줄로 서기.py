import sys

n = int(sys.stdin.readline())
higher_left = list(map(int, sys.stdin.readline().split()))  # 기본 인덱스
line = [0]*n
for i in range(n):
    cnt = 0
    index = higher_left[i]

    for j in range(n):
        if line[j] == 0:
            if cnt == index:
                line[j] = i+1
                break
            cnt += 1

print(*line)
