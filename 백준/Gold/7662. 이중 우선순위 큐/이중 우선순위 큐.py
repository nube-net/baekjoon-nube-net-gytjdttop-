# 확인용 코드 공부후 다시 제출예정
#https://ant-hill.tistory.com/170
import sys

input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    minQ, maxQ = [], []
    # 각 노드의 id에 대해 삭제되었는지 아닌지를 저장
    # 처음에는 아무 값도 없으므로 모두 삭제된 것으로 간주
    deleted = [True] * k
    for i in range(k):
        com, n = input().split()
        n = int(n)
        if com == 'I':
            heapq.heappush(minQ, (n, i))
            heapq.heappush(maxQ, (-n, i))
            deleted[i] = False
        else:
            if n == 1:
                # 삭제되지 않은 값 찾기
                # 삭제된 값은 힙에서 제거
                while maxQ and deleted[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    deleted[maxQ[0][1]] = True
                    heapq.heappop(maxQ)
            else:
                while minQ and deleted[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    deleted[minQ[0][1]] = True
                    heapq.heappop(minQ)

    # 연산이 끝난 후 삭제된 값들 제거
    while minQ and deleted[minQ[0][1]]:
        heapq.heappop(minQ)
    while maxQ and deleted[maxQ[0][1]]:
        heapq.heappop(maxQ)

    if minQ and maxQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print('EMPTY')