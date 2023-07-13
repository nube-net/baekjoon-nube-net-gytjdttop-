import sys
inputF = sys.stdin.readline  # 편의성

def code(a):
    while graph[a]:
        i= graph[a].pop()
        if i in Map:
            continue
        else :
            Map.add(i)
            code(i)


# 컴퓨터 수, 연결쌍 수 입력
n = int(inputF())
m = int(inputF())

# 그래프, 방문 기록
graph = []
Map = set()
Map.add(1)
for o in range(n+1):
    graph.append(set())

# 연결쌍 입력 후 그래프 저장
for i in range(m):
    x, y = map(int, inputF().split())
    graph[x].add(y)
    graph[y].add(x)


code(1)
print(len(Map)-1)