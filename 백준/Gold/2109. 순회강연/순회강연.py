import sys
from heapq import heappop, heappush, heapify
inputF = sys.stdin.readline

n = int(inputF())
lecture = []
for _ in range(n):
    x, y = map(int, inputF().split())
    lecture.append((y, x))

heapify(lecture)
money = []
heapify(money)
while lecture:
    time, price = heappop(lecture)
    if len(money) < time:
        heappush(money, price)
    else:
        if money[0] < price:
            heappop(money)
            heappush(money, price)

print(sum(money))