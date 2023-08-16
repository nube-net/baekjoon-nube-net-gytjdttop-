import sys
input = sys.stdin.readline
# 3차원 배열 구현 참고함 https://door-of-tabris.tistory.com/entry/%EB%B0%B1%EC%A4%80-15806%EB%B2%88-%EC%98%81%EC%9A%B0%EC%9D%98-%EA%B8%B0%EC%88%99%EC%82%AC%EC%B2%AD%EC%86%8C%ED%8C%8C%EC%9D%B4%EC%8D%AC)

# 방의 크기, 초기 곰팡이 위치의 수, 청소 지점의 수, 청소까지의 시간 입력 받기
n, m, k, time = map(int, input().split())

# 이동 방향 설정
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

# 초기 세팅
Q_mold = set()  # 확산해야 할 곰팡이 위치
clean = set()   # 청소해야 할 위치
visited = [[[False] * 2 for _ in range(n)] for _ in range(n)]

# 초기 곰팡이 위치 입력
for _ in range(m): 
    x, y = map(int, input().split())
    Q_mold.add((x-1, y-1, 0))
    visited[x-1][y-1][0] = True

# 청소 지점 입력
for _ in range(k): 
    x, y = map(int, input().split())
    clean.add((x-1, y-1))

# 곰팡이 확산
while Q_mold:
    x, y, day = Q_mold.pop()

    if day >= time:
        continue

    expand = False
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        next_day = (day + 1) % 2

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny][next_day]:
            visited[nx][ny][next_day] = True
            Q_mold.add((nx, ny, day + 1))
            expand = True

    # 확산이 없으면 현재 위치 곰팡이 제거
    if not expand:
        visited[x][y][day % 2] = False

# 청소 지점 검사
current_day = time % 2
for location in clean:
    if visited[location[0]][location[1]][current_day]:
        print('YES')
        break
else:
    print('NO')
