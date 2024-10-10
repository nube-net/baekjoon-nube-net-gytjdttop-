import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
tmp = 0
pre = arr[0]
flag = True
# 대칭성 이용, 상승 직선 시작 디폴트
# 하강직선 시작 -> 뒤집기, 상승직선 마무리 -> 옮기기 (각각 연산 +1) 
for i in range(1, n):
    cur = arr[i]
    
    if flag:
        if pre > cur:  # 윗방향 꼭짓점
            cnt += 1 # 상승 직선 개수
            flag = False  
    if not flag:
        if pre < cur:
            flag = True
    pre = cur
    
if flag:  # 자투리 처리
    cnt += int(bool(cnt))

ans = 0
while cnt > 1:
    cnt = cnt//2 + cnt%2  # 연산 + 자투리 직선 처리
    ans += 1
print(ans+cnt)
