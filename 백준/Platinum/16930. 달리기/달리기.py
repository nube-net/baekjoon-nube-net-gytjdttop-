import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int,input().split())
a = [list(input().rstrip()) for _ in range(n)]
s1, s2, d1, d2 = map(int,input().split())

q = deque()
visit = [[False for _ in range(m)] for _ in range(n)]
D = [(1,0), (-1,0), (0,-1), (0,1)]
ans = 0
visit[s1-1][s2-1] = True
q.append([s1-1,s2-1])
tmp = set()  # visit 처리할 인덱스
while q:
    l = len(q)
    ans += 1
    for _ in range(l):
        cur = q.popleft()
        
        for x,y in D:
            X = int(cur[0])
            Y = int(cur[1])
            for i in range(1,k+1):
                X += x
                Y += y
                if (X,Y,x,y) in tmp:
                    break
                if X <0 or Y < 0 or X >= n or Y>=m:
                    break
                if a[X][Y] == "#" or visit[X][Y]:
                    break
                if X == d1-1 and Y == d2-1:
                    print(ans)
                    exit()
                tmp.add((X,Y,x,y))
                q.append([X,Y])
    while tmp:
        cur = tmp.pop()
        visit[cur[0]][cur[1]] = True
    
print(-1)

    


