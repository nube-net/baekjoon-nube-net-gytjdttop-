import sys
input = sys.stdin.readline

n = int(input())
beads = [int(input()) for _ in range(n)]
beads.sort()
MAX = beads[-1]
if 2*MAX >= sum(beads):
    print(2*MAX-sum(beads))
else:
    if sum(beads)%2 == 0:
        print(0)
    else:
        print(1)