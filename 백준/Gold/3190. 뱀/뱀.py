import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
apple = set(tuple(map(int, input().split())) for _ in range(k))
L = int(input())
direction = deque(list(map(str, input().split())) for _ in range(L))

snake = deque()
snake.append((1,1))
dx = [0, -1, 0, 1]  # L -> idx 우측 이동
dy = [1, 0, -1, 0]
idx = 0

time = 0
tmp = direction.popleft()  # 정보
while True:
    time += 1

    x, y = snake[-1]
    if x + dx[idx] < 1 or y + dy[idx] < 1 or x + dx[idx] > n or y + dy[idx] > n:
        break  # 벽
    if (x + dx[idx], y + dy[idx]) in snake:
        break  # 몸통

    snake.append((x + dx[idx], y + dy[idx]))  # 머리 이동

    if (x + dx[idx], y + dy[idx]) in apple:
        apple. remove((x + dx[idx], y + dy[idx]))
    else:
        snake.popleft()  # 꼬리 이동

    if time == int(tmp[0]):  # 방향 전환
        if tmp[1] == 'L':
            idx += 1
            if idx > 3:
                idx = 0
            if direction:
                tmp = direction.popleft()
        else:
            idx -= 1
            if idx < 0:
                idx = 3
            if direction:
                tmp = direction.popleft()

print(time)