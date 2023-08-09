import sys
from heapq import heappop, heappush, heapify
inputF = sys.stdin.readline

n, m = map(int, inputF().split())
cards = list(map(int, inputF().split()))

heapify(cards)
for _ in range(m):
    a = heappop(cards)
    b = heappop(cards)
    heappush(cards, a+b)
    heappush(cards, a+b)

print(sum(cards))