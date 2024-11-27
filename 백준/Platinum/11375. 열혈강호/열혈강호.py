import sys
input = sys.stdin.readline
# 이분 매칭 - dfs

def dfs(person):
    for task in people[person]:
        if visited[task]:
            continue
        visited[task] = True
        # 만약 해당 작업이 아직 매칭되지 않았거나, 이전 사람을 다른 작업으로 매칭할 수 있다면
        if match[task] == -1 or dfs(match[task]):
            match[task] = person
            return True
    return False

n, m = map(int, input().split())
people = [[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    people[i] = tmp[1:]

match = [-1 for _ in range(m+1)]  # 매칭 여부
ans = 0

for person in range(1, n+1):
    visited = [False for _ in range(m+1)]  # 방문 여부 초기화
    if dfs(person):
        ans += 1

print(ans)
