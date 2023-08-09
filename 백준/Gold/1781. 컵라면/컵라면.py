import sys
from heapq import heappop, heappush, heapify
inputF = sys.stdin.readline
# 크게 만들기 문제 비슷한 아이디어

n = int(inputF())

foods = []
for i in range(n):
    x, y = map(int, inputF().split())
    foods.append((x, y))  # 데드 라인, 컵라면 수
heapify(foods)  # 1차 정렬(데드라인 오름차순)

result = []
heapify(result)
while foods:
    tmp = heappop(foods)
    if tmp[0] > len(result):
        heappush(result, tmp[1]) #2차 정렬(컵라면 개수 기준)
    else:
        tmp0 = heappop(result)
        if tmp0 < tmp[1]:
            heappush(result, tmp[1])
        else:
            heappush(result, tmp0)

print(sum(result))



