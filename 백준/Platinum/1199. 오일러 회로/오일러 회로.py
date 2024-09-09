import sys
input = sys.stdin.readline

n = int(input())
g = {}

for i in range(n):
    tmp = list(map(int, input().split()))
    g[i] = {}
    for j in range(n):
        if tmp[j]:
            g[i][j] = tmp[j]  # i에서 j로 가는 간선의 개수 tmp[j]개

st = -1

def count(g):
    global st
    for i in range(n):
        cnt = 0  # 정점의 차수 계산
        for k in g[i]:
            cnt += g[i][k]
        if cnt & 1:  # 차수가 홀수면 False 반환
            return False
        if st == -1 and cnt > 0:
            st = i
    return True

def dfs_stack(start):
    stack = [start]
    path = []
    ######################3
    while stack:
        cur = stack[-1]
        for nxt in g[cur]:
            if g[cur][nxt] > 0:
                g[cur][nxt] -= 1
                g[nxt][cur] -= 1
                stack.append(nxt)

                if g[cur][nxt] == 0:
                    g[cur].pop(nxt)
                    g[nxt].pop(cur)
                break
        else:
            path.append(stack.pop())
    #####################
    for node in path:
        print(node + 1, end=" ")

if count(g):
    dfs_stack(st)
else:
    print(-1)
