import sys
from heapq import heappop, heappush, heapify
inputF = sys.stdin.readline

# 입력
# 이동 가능 거리 중 최대 연료 주유소 선택
n = int(inputF())  # 주유소 개수
heap1 = []  # 1차 정렬
for _ in range(n):
    x, y = map(int, inputF().split())
    heappush(heap1, (x, y))  # 튜플 형태 저장
R, fuel = map(int, inputF().split())  # R 남은 마을 거리 fuel 연료

# 정렬 및 계산
key = False
d = 0  # 현재 위치
tmp = []  # 연료로 가능한 주유소
count = 0
while fuel < R and (key == False):

    # 주유소 선별
    while True:
        if heap1:
            x, y = heappop(heap1)
            if x <= fuel:  # 이동 가능 주유소
                heappush(tmp, (-y, x))  # 연료량 우선 순위
            else:  # 연료 불충분 거리
                heappush(heap1, (x, y))  # 되돌려 놓고 종료
                break
        else:
            break
    if tmp :
        y, x = heappop(tmp)  # y 음수 상태
        count += 1
        fuel -= y
    else:
        key = True
        break
if key:
    print(-1)
else:
    print(count)
