import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

n = int(input())
Min = []
Max = []
heapify(Min)
heapify(Max)
for i in range(n):
    # 입력
    if (not Min) and (not Max):  # 초기에만
        heappush(Max, int(input()))
        mid = Max[0]
        print(mid)
        continue
    else:
        tmp = int(input())
        if tmp < mid:
            heappush(Min, -tmp)
            if len(Min)-len(Max) > 1:
                a = heappop(Min)
                heappush(Max, -a)
        else:
            heappush(Max, tmp)
            if len(Max)-len(Min) > 1:
                a = heappop(Max)
                heappush(Min, -a)

        # 출력
        if i%2 == 0:  # 홀수
            if len(Max)> len(Min):
                mid = Max[0]
                print(mid)
            else:
                mid = -Min[0]
                print(mid)
        else:  # 짝수
            mid = min(Max[0], -Min[0])
            print(mid)