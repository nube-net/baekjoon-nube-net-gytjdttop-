import sys
inputF = sys.stdin.readline
Q = {(0,0)}
distance = 1

n, m = map(int, inputF().split())

maze = []  # 2차원 배열
for _ in range(n):
    maze.append(list(inputF().rstrip()))

while Q:  # BFS
    tmpQ = set()
    distance += 1
    while Q:
        x, y = Q.pop()  # 큐 원소 팝
        
        # 상
        if int(x) != 0:
            if maze[int(x)-1][int(y)] == '1':
                maze[int(x) - 1][int(y)] = distance
                tmpQ.add((int(x)-1, int(y)))
        
        # 하        
        if int(x) != n-1:
            if maze[int(x)+1][int(y)] == '1':
                maze[int(x) + 1][int(y)] = distance
                tmpQ.add((int(x)+1, int(y)))
        
        # 좌
        if int(y) != 0:
            if maze[int(x)][int(y)-1] == '1':
                maze[int(x)][int(y)-1] = distance
                tmpQ.add((int(x), int(y)-1))
        
        # 우
        if int(y) != m-1:
            if maze[int(x)][int(y)+1] == '1':
                maze[int(x)][int(y)+1] = distance
                tmpQ.add((int(x), int(y)+1))
    Q.update(tmpQ)
print(maze[n-1][m-1])


