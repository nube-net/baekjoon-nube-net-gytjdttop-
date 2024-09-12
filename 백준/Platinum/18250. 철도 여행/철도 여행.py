import sys
input = sys.stdin.readline

def find(a):
    if S[a] != a:
        S[a] = find(S[a])
    return S[a]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a > root_b:
        root_a, root_b = root_b, root_a
    S[root_b] = root_a

v, e = map(int, input().split())
S = [i for i in range(v+1)]  # 부모
arr = [0 for _ in range(v+1)]  # 차수
for _ in range(e):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] += 1
    union(a, b)

# 모든 노드가 같은 집합에 속하는지 확인
is_connected = True
dic ={}
tmp = set()
for i in range(1, v+1):
    cur = find(i)
    if arr[i] == 0:
        continue
    if cur in dic:
        dic[cur].append(i)
    else:
        dic[cur] = [i]

ans = 0
# 홀수 차수 노드 개수
for j in dic:
    odd_cnt = 0
    for i in dic[j]:
        if arr[i] % 2 == 1:
            odd_cnt += 1

    if (odd_cnt == 0 or odd_cnt == 2):
        ans += 1
    else:
        ans += odd_cnt//2 + odd_cnt%2
print(ans)
